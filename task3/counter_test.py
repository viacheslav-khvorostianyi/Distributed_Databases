import hazelcast
import threading
import time
import sys


def create_hazelcast_client():
    client = hazelcast.HazelcastClient(
        cluster_name="counter-cluster",
        cluster_members=[
            "172.28.0.11:5701",
            "172.28.0.12:5701",
            "172.28.0.13:5701"
        ],
        lifecycle_listeners=[
            lambda state: print(f"Client state changed to: {state}")
        ]
    )
    return client


def test_no_locking(client):
    """Test counter without any locking (will have race conditions)"""
    print("\n" + "="*80)
    print("TEST 1: Counter WITHOUT Locking")
    print("="*80)

    counter_map = client.get_map("counter-no-lock").blocking()
    counter_map.put("counter", 0)

    def increment_no_lock(iterations):
        for _ in range(iterations):
            current = counter_map.get("counter") or 0
            counter_map.put("counter", current + 1)

    threads = []
    start_time = time.time()

    for i in range(10):
        t = threading.Thread(target=increment_no_lock, args=(10000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.time() - start_time
    final_value = counter_map.get("counter")

    print(f"Expected: 100,000")
    print(f"Got:      {final_value:,}")
    print(f"Time:     {elapsed:.2f} seconds")
    print(f"Correct:  {'✓' if final_value == 100000 else '✗'}")

    return final_value == 100000, elapsed


def test_pessimistic_locking(client):
    """Test counter with pessimistic locking"""
    print("\n" + "="*80)
    print("TEST 2: Counter WITH Pessimistic Locking")
    print("="*80)

    counter_map = client.get_map("counter-pessimistic").blocking()
    counter_map.put("counter", 0)

    def increment_pessimistic(iterations):
        for _ in range(iterations):
            counter_map.lock("counter")
            try:
                current = counter_map.get("counter") or 0
                counter_map.put("counter", current + 1)
            finally:
                counter_map.unlock("counter")

    threads = []
    start_time = time.time()

    for i in range(10):
        t = threading.Thread(target=increment_pessimistic, args=(10000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.time() - start_time
    final_value = counter_map.get("counter")

    print(f"Expected: 100,000")
    print(f"Got:      {final_value:,}")
    print(f"Time:     {elapsed:.2f} seconds")
    print(f"Correct:  {'✓' if final_value == 100000 else '✗'}")

    return final_value == 100000, elapsed


def test_optimistic_locking(client):
    """Test counter with optimistic locking (compare-and-swap)"""
    print("\n" + "="*80)
    print("TEST 3: Counter WITH Optimistic Locking")
    print("="*80)

    counter_map = client.get_map("counter-optimistic").blocking()
    counter_map.put("counter", 0)

    def increment_optimistic(iterations):
        for _ in range(iterations):
            while True:
                current = counter_map.get("counter") or 0
                if counter_map.replace_if_same("counter", current, current + 1):
                    break
                # If replacement failed, retry

    threads = []
    start_time = time.time()

    for i in range(10):
        t = threading.Thread(target=increment_optimistic, args=(10000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.time() - start_time
    final_value = counter_map.get("counter")

    print(f"Expected: 100,000")
    print(f"Got:      {final_value:,}")
    print(f"Time:     {elapsed:.2f} seconds")
    print(f"Correct:  {'✓' if final_value == 100000 else '✗'}")

    return final_value == 100000, elapsed


def test_iatomic_long(client):
    """Test counter with IAtomicLong (CP Subsystem)"""
    print("\n" + "="*80)
    print("TEST 4: Counter WITH IAtomicLong (CP Subsystem)")
    print("="*80)

    atomic_counter = client.cp_subsystem.get_atomic_long("counter").blocking()
    atomic_counter.set(0)

    def increment_atomic(iterations):
        for _ in range(iterations):
            atomic_counter.increment_and_get()

    threads = []
    start_time = time.time()

    for i in range(10):
        t = threading.Thread(target=increment_atomic, args=(10000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.time() - start_time
    final_value = atomic_counter.get()

    print(f"Expected: 100,000")
    print(f"Got:      {final_value:,}")
    print(f"Time:     {elapsed:.2f} seconds")
    print(f"Correct:  {'✓' if final_value == 100000 else '✗'}")

    return final_value == 100000, elapsed


def test_pessimistic_with_failure(client):
    """Test pessimistic locking with node failure"""
    print("\n" + "="*80)
    print("TEST 5: Pessimistic Locking WITH Node Failure")
    print("="*80)
    print("NOTE: To test this, kill one node (e.g., docker kill hazelcast-node2)")
    print("      during execution. The test will wait 5 seconds before starting.")

    time.sleep(5)

    counter_map = client.get_map("counter-pessimistic-fail").blocking()
    counter_map.put("counter", 0)

    def increment_pessimistic(iterations):
        for _ in range(iterations):
            try:
                counter_map.lock("counter")
                try:
                    current = counter_map.get("counter") or 0
                    counter_map.put("counter", current + 1)
                finally:
                    counter_map.unlock("counter")
            except Exception as e:
                print(f"Error during increment: {e}")

    threads = []
    start_time = time.time()

    for i in range(10):
        t = threading.Thread(target=increment_pessimistic, args=(10000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.time() - start_time
    final_value = counter_map.get("counter")

    print(f"Expected: 100,000")
    print(f"Got:      {final_value:,}")
    print(f"Time:     {elapsed:.2f} seconds")
    print(f"Correct:  {'✓' if final_value == 100000 else '✗'}")

    return final_value == 100000, elapsed


def test_optimistic_with_failure(client):
    """Test optimistic locking with node failure"""
    print("\n" + "="*80)
    print("TEST 6: Optimistic Locking WITH Node Failure")
    print("="*80)
    print("NOTE: To test this, kill one node (e.g., docker kill hazelcast-node2)")
    print("      during execution. The test will wait 5 seconds before starting.")

    time.sleep(5)

    counter_map = client.get_map("counter-optimistic-fail").blocking()
    counter_map.put("counter", 0)

    def increment_optimistic(iterations):
        for _ in range(iterations):
            while True:
                try:
                    current = counter_map.get("counter") or 0
                    if counter_map.replace_if_same("counter", current, current + 1):
                        break
                except Exception as e:
                    print(f"Error during increment: {e}")
                    break

    threads = []
    start_time = time.time()

    for i in range(10):
        t = threading.Thread(target=increment_optimistic, args=(10000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.time() - start_time
    final_value = counter_map.get("counter")

    print(f"Expected: 100,000")
    print(f"Got:      {final_value:,}")
    print(f"Time:     {elapsed:.2f} seconds")
    print(f"Correct:  {'✓' if final_value == 100000 else '✗'}")

    return final_value == 100000, elapsed


def test_iatomic_with_leader_failure(client):
    """Test IAtomicLong with leader node failure"""
    print("\n" + "="*80)
    print("TEST 7: IAtomicLong WITH Leader Node Failure")
    print("="*80)
    print("NOTE: Check logs to identify the LEADER of 'default' CP group")
    print("      Kill the leader node during execution.")
    print("      The test will wait 5 seconds before starting.")

    time.sleep(5)

    atomic_counter = client.cp_subsystem.get_atomic_long("counter-leader-fail").blocking()
    atomic_counter.set(0)

    def increment_atomic(iterations):
        for _ in range(iterations):
            try:
                atomic_counter.increment_and_get()
            except Exception as e:
                print(f"Error during increment: {e}")

    threads = []
    start_time = time.time()

    for i in range(10):
        t = threading.Thread(target=increment_atomic, args=(10000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.time() - start_time
    final_value = atomic_counter.get()

    print(f"Expected: 100,000")
    print(f"Got:      {final_value:,}")
    print(f"Time:     {elapsed:.2f} seconds")
    print(f"Correct:  {'✓' if final_value == 100000 else '✗'}")

    return final_value == 100000, elapsed


def test_redo_operation(client):
    """Test with redo operation enabled"""
    print("\n" + "="*80)
    print("TEST 8: IAtomicLong WITH Redo Operation Enabled")
    print("="*80)

    # Create a new client with redo operation enabled
    redo_client = hazelcast.HazelcastClient(
        cluster_name="counter-cluster",
        cluster_members=[
            "172.28.0.11:5701",
            "172.28.0.12:5701",
            "172.28.0.13:5701"
        ],
        redo_operation=True
    )

    try:
        atomic_counter = redo_client.cp_subsystem.get_atomic_long("counter-redo").blocking()
        atomic_counter.set(0)

        def increment_atomic(iterations):
            for _ in range(iterations):
                try:
                    atomic_counter.increment_and_get()
                except Exception as e:
                    print(f"Error during increment: {e}")

        threads = []
        start_time = time.time()

        for i in range(10):
            t = threading.Thread(target=increment_atomic, args=(10000,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        elapsed = time.time() - start_time
        final_value = atomic_counter.get()

        print(f"Expected: 100,000")
        print(f"Got:      {final_value:,}")
        print(f"Time:     {elapsed:.2f} seconds")
        print(f"Correct:  {'✓' if final_value == 100000 else '✗'}")

        return final_value == 100000, elapsed
    finally:
        redo_client.shutdown()


def main():
    """Main test runner"""
    print("="*80)
    print("TASK 3: Hazelcast Distributed Counter Tests")
    print("="*80)

    # Wait for Hazelcast cluster to be ready
    print("\nWaiting for Hazelcast cluster to be ready...")
    time.sleep(10)

    try:
        client = create_hazelcast_client()
        print("✓ Connected to Hazelcast cluster")

        results = []

        # Run all tests
        print("\n" + "="*80)
        print("Running all tests...")
        print("="*80)

        # Basic tests
        result1 = test_no_locking(client)
        results.append(("No Locking", result1))

        result2 = test_pessimistic_locking(client)
        results.append(("Pessimistic Locking", result2))

        result3 = test_optimistic_locking(client)
        results.append(("Optimistic Locking", result3))

        result4 = test_iatomic_long(client)
        results.append(("IAtomicLong", result4))

        # Summary
        print("\n" + "="*80)
        print("TEST SUMMARY")
        print("="*80)
        print(f"{'Test Name':<30} {'Correct':<10} {'Time (s)':<10}")
        print("-" * 80)
        for name, (correct, elapsed) in results:
            print(f"{name:<30} {'✓' if correct else '✗':<10} {elapsed:<10.2f}")

        client.shutdown()
        print("\n✓ Tests completed successfully")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

