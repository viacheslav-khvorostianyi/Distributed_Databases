from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement, ConsistencyLevel
import time
from datetime import datetime
import concurrent.futures
from typing import List, Tuple

class CassandraWebCounter:
    def __init__(self, hosts=['127.0.0.1'], keyspace='shop'):
        self.cluster = Cluster(hosts)
        self.session = self.cluster.connect()
        self.keyspace = keyspace
        self._setup_keyspace()
        self.session.set_keyspace(keyspace)
        self._setup_table()

    def _setup_keyspace(self):
        """Create keyspace if it doesn't exist"""
        self.session.execute(f"""
            CREATE KEYSPACE IF NOT EXISTS {self.keyspace}
            WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': 1}}
        """)

    def _setup_table(self):
        """Create counter table if it doesn't exist"""
        self.session.execute("""
            CREATE TABLE IF NOT EXISTS web_counters (
                counter_name TEXT PRIMARY KEY,
                count COUNTER
            )
        """)

    def increment(self, counter_name='page_views', increment_by=1):
        """Increment counter by specified value"""
        query = SimpleStatement(
            "UPDATE web_counters SET count = count + %s WHERE counter_name = %s",
            consistency_level=ConsistencyLevel.ONE
        )
        self.session.execute(query, [increment_by, counter_name])

    def get_count(self, counter_name='page_views'):
        """Get current counter value"""
        query = "SELECT count FROM web_counters WHERE counter_name = %s"
        result = self.session.execute(query, [counter_name])
        row = result.one()
        return row.count if row else 0

    def reset(self, counter_name='page_views'):
        """Reset counter to 0 by deleting the row"""
        query = "DELETE FROM web_counters WHERE counter_name = %s"
        self.session.execute(query, [counter_name])

    def close(self):
        self.cluster.shutdown()


def client_worker(client_id: int, num_requests: int, counter_name: str) -> Tuple[int, float, int, List[Exception]]:
    """
    Single client that performs num_requests increments
    Returns: (client_id, execution_time, successful_requests, errors)
    """
    counter = CassandraWebCounter()
    start_time = time.time()
    successful = 0
    errors = []

    try:
        for i in range(num_requests):
            try:
                counter.increment(counter_name)
                successful += 1
            except Exception as e:
                errors.append(e)
                if len(errors) <= 5:  # Log only first 5 errors
                    print(f"Client {client_id} error on request {i}: {e}")
    finally:
        counter.close()

    end_time = time.time()
    execution_time = end_time - start_time

    return client_id, execution_time, successful, errors


def run_performance_test(num_clients=10, requests_per_client=10000, counter_name='page_views'):
    """
    Run performance test with multiple concurrent clients
    """
    print(f"\n{'='*80}")
    print(f"Cassandra Counter Performance Test")
    print(f"{'='*80}")
    print(f"Configuration:")
    print(f"  - Clients:              {num_clients}")
    print(f"  - Requests per client:  {requests_per_client:,}")
    print(f"  - Total requests:       {num_clients * requests_per_client:,}")
    print(f"  - Counter name:         {counter_name}")
    print(f"{'='*80}\n")

    # Reset counter before test
    counter = CassandraWebCounter()
    counter.reset(counter_name)
    initial_count = counter.get_count(counter_name)
    print(f"Initial counter value: {initial_count}")
    print(f"Starting test at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    counter.close()

    # Start test
    overall_start = time.time()

    # Run clients concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_clients) as executor:
        futures = [
            executor.submit(client_worker, client_id, requests_per_client, counter_name)
            for client_id in range(1, num_clients + 1)
        ]

        results = [future.result() for future in concurrent.futures.as_completed(futures)]

    overall_end = time.time()
    total_time = overall_end - overall_start

    # Get final counter value
    counter = CassandraWebCounter()
    final_count = counter.get_count(counter_name)
    counter.close()

    # Analyze results
    print(f"\n{'='*80}")
    print("Individual Client Results:")
    print(f"{'='*80}\n")

    total_requests = 0
    total_successful = 0
    total_errors = 0

    print(f"{'Client':<10} {'Time (s)':<12} {'Successful':<12} {'Failed':<10} {'Req/s':<12}")
    print(f"{'-'*66}")

    for client_id, exec_time, successful, errors in sorted(results):
        rps = successful / exec_time if exec_time > 0 else 0
        failed = len(errors)
        print(f"{client_id:<10} {exec_time:<12.2f} {successful:<12,} {failed:<10} {rps:<12.2f}")
        total_requests += requests_per_client
        total_successful += successful
        total_errors += failed

    # Summary statistics
    print(f"\n{'='*80}")
    print("Performance Summary:")
    print(f"{'='*80}")
    print(f"Total requests:           {total_requests:,}")
    print(f"Successful requests:      {total_successful:,}")
    print(f"Failed requests:          {total_errors:,}")
    print(f"Success rate:             {(total_successful / total_requests * 100):.2f}%")
    print(f"\nCounter Statistics:")
    print(f"Expected counter value:   {total_successful:,}")
    print(f"Actual counter value:     {final_count:,}")
    print(f"Counter accuracy:         {(final_count / total_successful * 100):.4f}%")
    print(f"Missing increments:       {total_successful - final_count:,}")
    print(f"\nTiming:")
    print(f"Total execution time:     {total_time:.2f} seconds")
    print(f"Overall throughput:       {total_successful / total_time:.2f} req/s")
    print(f"Average time per client:  {total_time:.2f} seconds")
    print(f"Average latency:          {(total_time / total_successful) * 1000:.2f} ms/request")
    print(f"{'='*80}\n")

    return {
        'total_requests': total_requests,
        'successful_requests': total_successful,
        'failed_requests': total_errors,
        'final_count': final_count,
        'total_time': total_time,
        'throughput': total_successful / total_time,
        'accuracy': (final_count / total_successful * 100) if total_successful > 0 else 0
    }


def compare_configurations():
    """Compare different client/request configurations"""
    configurations = [
        (5, 20000),   # 5 clients × 20K requests
        (10, 10000),  # 10 clients × 10K requests
        (20, 5000),   # 20 clients × 5K requests
        (50, 2000),   # 50 clients × 2K requests
    ]

    comparison_results = []

    for num_clients, requests_per_client in configurations:
        print(f"\n\n{'#'*80}")
        print(f"Configuration: {num_clients} clients × {requests_per_client:,} requests")
        print(f"{'#'*80}")

        counter_name = f'test_{num_clients}c_{requests_per_client}r'
        results = run_performance_test(num_clients, requests_per_client, counter_name)
        results['config'] = f"{num_clients}c × {requests_per_client}r"
        comparison_results.append(results)

        time.sleep(2)  # Pause between tests

    # Print comparison
    print(f"\n{'='*80}")
    print("Configuration Comparison:")
    print(f"{'='*80}\n")
    print(f"{'Config':<20} {'Total Req':<12} {'Time (s)':<12} {'Throughput':<15} {'Accuracy':<12}")
    print(f"{'-'*80}")

    for result in comparison_results:
        print(f"{result['config']:<20} "
              f"{result['total_requests']:<12,} "
              f"{result['total_time']:<12.2f} "
              f"{result['throughput']:<15.2f} "
              f"{result['accuracy']:<12.2f}%")

    print(f"{'='*80}\n")

    # Find best configuration
    best_throughput = max(comparison_results, key=lambda x: x['throughput'])
    best_accuracy = max(comparison_results, key=lambda x: x['accuracy'])

    print("Best Results:")
    print(f"  Highest throughput: {best_throughput['config']} - {best_throughput['throughput']:.2f} req/s")
    print(f"  Best accuracy:      {best_accuracy['config']} - {best_accuracy['accuracy']:.4f}%")
    print()


if __name__ == "__main__":
    # Run single test with 10 clients × 10K requests
    print("Running primary test configuration...")
    results = run_performance_test(
        num_clients=10,
        requests_per_client=10000,
        counter_name='performance_test_10c_10k'
    )

    # Optional: Run comparison of different configurations
    # Uncomment the line below to run additional tests
    # compare_configurations()
