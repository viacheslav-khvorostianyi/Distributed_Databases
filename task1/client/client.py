import time
import argparse
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


def worker(url, n_requests):
    s = requests.Session()
    for i in range(n_requests):
        r = s.post(f"{url}/inc")
        r.raise_for_status()
    return True


def run_experiment(url, clients, requests_per_client):
    """Run a single experiment with specified number of clients"""
    print(f"\n{'='*60}")
    print(f"Running experiment: {clients} client(s), {requests_per_client} requests each")
    print(f"{'='*60}")

    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=clients) as ex:
        futures = [ex.submit(worker, url, requests_per_client) for _ in range(clients)]
        for f in as_completed(futures):
            f.result()
    end = time.perf_counter()
    elapsed = end - start

    # Get final count
    r = requests.get(f"{url}/count")
    r.raise_for_status()
    total_count = r.json().get("value", None)

    expected_count = clients * requests_per_client
    print(f"\nResults:")
    print(f"  Total count: {total_count}")
    print(f"  Expected count: {expected_count}")
    print(f"  Elapsed time: {elapsed:.4f} seconds")

    if elapsed > 0 and total_count is not None:
        throughput = total_count / elapsed
        print(f"  Throughput: {throughput:.2f} requests/second")

    if total_count != expected_count:
        print(f"  WARNING: Count mismatch! Lost {expected_count - total_count} updates")

    return {
        "clients": clients,
        "requests_per_client": requests_per_client,
        "total_count": total_count,
        "expected_count": expected_count,
        "elapsed": elapsed,
        "throughput": total_count / elapsed if elapsed > 0 else 0
    }


def reset_counter(url):
    """Reset the counter to 0"""
    try:
        r = requests.post(f"{url}/reset")
        r.raise_for_status()
        print("Counter reset successfully")
    except Exception as e:
        print(f"Warning: Could not reset counter: {e}")


def main():
    parser = argparse.ArgumentParser(description="Web counter client for load testing")
    parser.add_argument("--url", default="http://127.0.0.1:8080", help="Server URL")
    parser.add_argument("--clients", type=int, help="Number of concurrent clients")
    parser.add_argument("--requests-per-client", type=int, default=10000, help="Requests per client")
    parser.add_argument("--run-all", action="store_true", help="Run all experiments (1, 2, 5 clients)")
    args = parser.parse_args()

    if args.run_all:
        # Run all experiments
        experiments = [1, 2, 5]
        results = []

        print(f"\n{'#'*60}")
        print(f"# Running all experiments with {args.requests_per_client} requests per client")
        print(f"# Server: {args.url}")
        print(f"{'#'*60}")

        for num_clients in experiments:
            # Reset counter before each experiment
            reset_counter(args.url)
            time.sleep(0.5)  # Small delay to ensure reset completes

            result = run_experiment(args.url, num_clients, args.requests_per_client)
            results.append(result)

        # Summary
        print(f"\n{'='*60}")
        print(f"SUMMARY OF ALL EXPERIMENTS")
        print(f"{'='*60}")
        print(f"{'Clients':<10} {'Total Req':<12} {'Time (s)':<12} {'Throughput (req/s)':<20}")
        print(f"{'-'*60}")
        for r in results:
            print(f"{r['clients']:<5} {r['total_count']:<12} {r['elapsed']:<12.4f} {r['throughput']:<20.2f}")

    elif args.clients:
        # Run single experiment
        run_experiment(args.url, args.clients, args.requests_per_client)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

