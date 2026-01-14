import hazelcast
import threading
import time
import sys


def create_client():
    return hazelcast.HazelcastClient(
        cluster_name="counter-cluster",
        cluster_members=[
            "172.28.0.11:5701",
            "172.28.0.12:5701",
            "172.28.0.13:5701"
        ]
    )


def test_pessimistic_with_failure():
    print("="*80)
    print("FAILURE TEST: Pessimistic Locking")
    print("="*80)
    print("\nInstructions:")
    print("1. This test will start incrementing a counter")
    print("2. After 5 seconds, kill one node: docker kill hazelcast-node2")
    print("3. Observe the behavior")
    print("\nStarting in 3 seconds...")
    time.sleep(3)

    client = create_client()
    counter_map = client.get_map("counter-fail-pessimistic").blocking()
    counter_map.put("counter", 0)

    completed_increments = [0]
    errors = [0]

    def increment_pessimistic(iterations):
        for i in range(iterations):
            try:
                counter_map.lock("counter")
                try:
                    current = counter_map.get("counter") or 0
                    counter_map.put("counter", current + 1)
                    completed_increments[0] += 1
                finally:
                    counter_map.unlock("counter")
            except Exception as e:
                errors[0] += 1
                if errors[0] <= 5:
                    print(f"Error at iteration {i}: {e}")

            if i % 10000 == 0 and i > 0:
                print(f"Completed {i} iterations...")

    print("\nStarting counter increments...")
    print("KILL A NODE NOW: docker kill hazelcast-node2\n")

    threads = []
    start_time = time.time()

    for _ in range(10):
        t = threading.Thread(target=increment_pessimistic, args=(10000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.time() - start_time
    final_value = counter_map.get("counter")

    print("\n" + "="*80)
    print("RESULTS")
    print("="*80)
    print(f"Expected:            100,000")
    print(f"Final value:         {final_value:,}")
    print(f"Completed increments: {completed_increments[0]:,}")
    print(f"Errors:              {errors[0]:,}")
    print(f"Time:                {elapsed:.2f} seconds")
    print(f"Correct:             {'✓' if final_value == 100000 else '✗'}")

    client.shutdown()


def test_optimistic_with_failure():
    print("=" * 80)
    print("FAILURE TEST: Optimistic Locking")
    print("=" * 80)
    print("\nInstructions:")
    print("1. This test will start incrementing a counter")
    print("2. After 5 seconds, kill one node: docker kill hazelcast-node2")
    print("3. Observe the behavior and retry mechanism")
    print("\nStarting in 3 seconds...")
    time.sleep(3)

    client = create_client()
    counter_map = client.get_map("counter-fail-optimistic").blocking()
    counter_map.put("counter", 0)

    completed_increments = [0]
    errors = [0]
    retries = [0]

    def increment_optimistic(iterations):
        for i in range(iterations):
            max_retries = 100
            retry_count = 0

            while retry_count < max_retries:
                try:
                    old_value = counter_map.get("counter") or 0
                    new_value = old_value + 1

                    if counter_map.replace_if_same("counter", old_value, new_value):
                        completed_increments[0] += 1
                        if retry_count > 0:
                            retries[0] += retry_count
                        break
                    else:
                        retry_count += 1
                except Exception as e:
                    errors[0] += 1
                    if errors[0] <= 5:
                        print(f"Error at iteration {i}: {e}")
                    retry_count += 1
                    time.sleep(0.01)

            if retry_count >= max_retries:
                print(f"Failed after {max_retries} retries at iteration {i}")

            if i % 10000 == 0 and i > 0:
                print(f"Completed {i} iterations...")

    print("\nStarting counter increments...")
    print("KILL A NODE NOW: docker kill hazelcast-node2\n")

    threads = []
    start_time = time.time()

    for _ in range(10):
        t = threading.Thread(target=increment_optimistic, args=(10000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.time() - start_time
    final_value = counter_map.get("counter")

    print("\n" + "=" * 80)
    print("RESULTS")
    print("=" * 80)
    print(f"Expected:            100,000")
    print(f"Final value:         {final_value:,}")
    print(f"Completed increments: {completed_increments[0]:,}")
    print(f"Total retries:       {retries[0]:,}")
    print(f"Errors:              {errors[0]:,}")
    print(f"Time:                {elapsed:.2f} seconds")
    print(f"Correct:             {'✓' if final_value == 100000 else '✗'}")

    client.shutdown()


def test_iatomic_with_leader_failure():
    print("="*80)
    print("FAILURE TEST: IAtomicLong with Leader Failure")
    print("="*80)
    print("\nInstructions:")
    print("1. Check logs to find the CP group LEADER")
    print("   docker logs hazelcast-node1 2>&1 | grep 'LEADER'")
    print("2. After 5 seconds, kill the LEADER node")
    print("3. Observe automatic leader election and continuation")
    print("\nStarting in 3 seconds...")
    time.sleep(3)

    client = create_client()
    atomic_counter = client.cp_subsystem.get_atomic_long("counter-fail-leader").blocking()
    atomic_counter.set(0)

    completed_increments = [0]
    errors = [0]

    def increment_atomic(iterations):
        for i in range(iterations):
            try:
                atomic_counter.increment_and_get()
                completed_increments[0] += 1
            except Exception as e:
                errors[0] += 1
                if errors[0] <= 5:
                    print(f"Error at iteration {i}: {e}")
                # Retry after error
                time.sleep(0.1)

            if i % 10000 == 0 and i > 0:
                print(f"Completed {i} iterations...")

    print("\nStarting counter increments...")
    print("KILL THE LEADER NODE NOW!\n")

    threads = []
    start_time = time.time()

    for _ in range(10):
        t = threading.Thread(target=increment_atomic, args=(10000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.time() - start_time
    final_value = atomic_counter.get()

    print("\n" + "="*80)
    print("RESULTS")
    print("="*80)
    print(f"Expected:            100,000")
    print(f"Final value:         {final_value:,}")
    print(f"Completed increments: {completed_increments[0]:,}")
    print(f"Errors:              {errors[0]:,}")
    print(f"Time:                {elapsed:.2f} seconds")
    print(f"Correct:             {'✓' if final_value == 100000 else '✗'}")

    client.shutdown()


def main():
    if len(sys.argv) < 2:
        print("Usage: python failure_test.py [pessimistic|optimistic|iatomic]")
        print("")
        print("Tests:")
        print("  pessimistic - Test pessimistic locking with node failure")
        print("  optimistic  - Test optimistic locking with node failure")
        print("  iatomic     - Test IAtomicLong with leader failure")
        sys.exit(1)

    test_type = sys.argv[1].lower()

    print("\nWaiting for Hazelcast cluster...")
    time.sleep(5)

    if test_type == "pessimistic":
        test_pessimistic_with_failure()
    elif test_type == "optimistic":
        test_optimistic_with_failure()
    elif test_type == "iatomic":
        test_iatomic_with_leader_failure()
    else:
        print(f"Unknown test type: {test_type}")
        sys.exit(1)



if __name__ == "__main__":
    main()

