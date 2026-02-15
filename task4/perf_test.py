import concurrent.futures
import time
from pymongo import MongoClient
import statistics


class CounterPerformanceTest:
    def __init__(self, num_clients=10, calls_per_client=10000, uri="mongodb://admin:password@localhost:27017/"):
        self.num_clients = num_clients
        self.calls_per_client = calls_per_client
        self.uri = uri
        # Connection pooling settings with write concern
        self.client = MongoClient(
            uri,
            maxPoolSize=num_clients + 5,
            minPoolSize=1,
            w='majority',  # Write concern - wait for majority acknowledgment
            journal=True   # Wait for journal write
        )
        self.db = self.client["counter_db"]
        self.collection = self.db["counters"]
        self.reset_counter()

    def reset_counter(self):
        """Reset counter before test and initialize document"""
        self.collection.delete_many({})
        # Pre-create the counter document to avoid upsert race conditions
        self.collection.insert_one({"counter_id": "default", "count": 0})

    def worker(self, client_id):
        """Single client making multiple increment calls using shared connection pool"""
        # Reuse shared connection pool for proper concurrency and consistency
        collection = self.db["counters"]

        times = []
        start_total = time.perf_counter()

        for i in range(self.calls_per_client):
            start = time.perf_counter()
            # Update without upsert since document is pre-created
            result = collection.find_one_and_update(
                {"counter_id": "default"},
                {"$inc": {"count": 1}},
                return_document=True
            )
            if result is None:
                raise Exception(f"Counter document not found for client {client_id} at iteration {i}")
            elapsed = time.perf_counter() - start
            times.append(elapsed)

        total_time = time.perf_counter() - start_total

        return {
            "client_id": client_id,
            "total_time": total_time,
            "times": times
        }

    def run_test(self):
        """Run performance test with concurrent clients"""
        print(f"Starting performance test...")
        print(f"Clients: {self.num_clients}, Calls per client: {self.calls_per_client}")
        print(f"Total operations: {self.num_clients * self.calls_per_client}\n")

        test_start = time.perf_counter()

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.num_clients) as executor:
            results = list(executor.map(self.worker, range(self.num_clients)))
            executor.shutdown(wait=True)  # Ensure all threads complete

        test_total = time.perf_counter() - test_start

        # Verify final count - all operations should be complete
        final_doc = self.collection.find_one({"counter_id": "default"})
        final_count = final_doc["count"] if final_doc else 0
        expected_count = self.num_clients * self.calls_per_client

        self._print_results(results, test_total, final_count, expected_count)

    def _print_results(self, results, test_total, final_count, expected_count):
        """Print performance test results"""
        all_times = []
        for r in results:
            all_times.extend(r["times"])

        print("=" * 60)
        print("PERFORMANCE TEST RESULTS")
        print("=" * 60)
        print(f"Total execution time: {test_total:.2f} seconds")
        print(f"Throughput: {(self.num_clients * self.calls_per_client / test_total):.0f} ops/sec\n")

        print("Counter Verification:")
        print(f"Expected count: {expected_count}")
        print(f"Final count: {final_count}")
        print(f"Match: {'✓ YES' if final_count == expected_count else '✗ NO'}\n")

        print("Per-Operation Statistics (in seconds):")
        print(f"Min: {min(all_times):.6f}")
        print(f"Max: {max(all_times):.6f}")
        print(f"Avg: {statistics.mean(all_times):.6f}")
        print(f"Median: {statistics.median(all_times):.6f}")
        print(f"Std Dev: {statistics.stdev(all_times):.6f}")
        print("=" * 60)

        print("\nPer-Client Statistics:")
        for r in results:
            print(f"Client {r['client_id']}: {r['total_time']:.2f}s")

    def close(self):
        self.client.close()


if __name__ == "__main__":
    test = CounterPerformanceTest(num_clients=10, calls_per_client=10000)
    test.run_test()
    test.close()
