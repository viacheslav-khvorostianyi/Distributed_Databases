import psycopg2
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable


class DatabaseConfig:
    """Database connection configuration"""
    def __init__(self, host="postgres", port=5432, database="counter_db",
                 user="postgres", password="postgres"):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def get_connection(self):
        """Create a new database connection"""
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )


def reset_counter(db_config: DatabaseConfig):
    """Reset counter to 0"""
    conn = db_config.get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE user_counter SET counter = 0, version = 0 WHERE user_id = 1")
        conn.commit()
        print("Counter reset to 0")
    finally:
        conn.close()


def get_counter_value(db_config: DatabaseConfig) -> int:
    """Get current counter value"""
    conn = db_config.get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT counter FROM user_counter WHERE user_id = 1")
        result = cursor.fetchone()
        return result[0] if result else 0
    finally:
        conn.close()


# ============================================================
# VARIANT 1: Lost Update (will lose updates!)
# ============================================================

def lost_update_worker(db_config: DatabaseConfig, iterations: int):
    """Worker for lost update variant - NOT thread-safe!"""
    conn = db_config.get_connection()
    try:
        cursor = conn.cursor()
        for i in range(iterations):
            # Read current value
            cursor.execute("SELECT counter FROM user_counter WHERE user_id = 1")
            counter = cursor.fetchone()[0]

            # Increment
            counter = counter + 1

            # Write back (RACE CONDITION HERE!)
            cursor.execute("UPDATE user_counter SET counter = %s WHERE user_id = 1", (counter,))
            conn.commit()
    finally:
        conn.close()


# ============================================================
# VARIANT 2: Serializable Isolation Level
# ============================================================

def serializable_worker(db_config: DatabaseConfig, iterations: int):
    """Worker with SERIALIZABLE isolation level"""
    conn = db_config.get_connection()
    try:
        for i in range(iterations):
            while True:
                try:
                    # Set isolation level to SERIALIZABLE
                    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE)
                    cursor = conn.cursor()

                    # Read current value
                    cursor.execute("SELECT counter FROM user_counter WHERE user_id = 1")
                    counter = cursor.fetchone()[0]

                    # Increment
                    counter = counter + 1

                    # Write back
                    cursor.execute("UPDATE user_counter SET counter = %s WHERE user_id = 1", (counter,))
                    conn.commit()
                    break  # Success, exit retry loop

                except psycopg2.extensions.TransactionRollbackError:
                    # Serialization failure - retry
                    conn.rollback()
                    continue
    finally:
        conn.close()


# ============================================================
# VARIANT 3: In-place Update (atomic increment)
# ============================================================

def inplace_update_worker(db_config: DatabaseConfig, iterations: int):
    """Worker with in-place atomic update - thread-safe!"""
    conn = db_config.get_connection()
    try:
        cursor = conn.cursor()
        for i in range(iterations):
            # Atomic increment
            cursor.execute("UPDATE user_counter SET counter = counter + 1 WHERE user_id = 1")
            conn.commit()
    finally:
        conn.close()


# ============================================================
# VARIANT 4: Row-level Locking (SELECT ... FOR UPDATE)
# ============================================================

def row_locking_worker(db_config: DatabaseConfig, iterations: int):
    """Worker with row-level locking using FOR UPDATE"""
    conn = db_config.get_connection()
    try:
        for i in range(iterations):
            cursor = conn.cursor()

            # Lock the row for update
            cursor.execute("SELECT counter FROM user_counter WHERE user_id = 1 FOR UPDATE")
            counter = cursor.fetchone()[0]

            # Increment
            counter = counter + 1

            # Write back
            cursor.execute("UPDATE user_counter SET counter = %s WHERE user_id = 1", (counter,))
            conn.commit()
    finally:
        conn.close()


# ============================================================
# VARIANT 5: Optimistic Concurrency Control
# ============================================================

def optimistic_locking_worker(db_config: DatabaseConfig, iterations: int):
    """Worker with optimistic locking using version field"""
    conn = db_config.get_connection()
    try:
        cursor = conn.cursor()
        for i in range(iterations):
            while True:
                # Read current value and version
                cursor.execute("SELECT counter, version FROM user_counter WHERE user_id = 1")
                counter, version = cursor.fetchone()

                # Increment
                counter = counter + 1

                # Try to update with version check
                cursor.execute(
                    "UPDATE user_counter SET counter = %s, version = %s WHERE user_id = %s AND version = %s",
                    (counter, version + 1, 1, version)
                )
                conn.commit()

                # Check if update was successful
                if cursor.rowcount > 0:
                    break  # Success, exit retry loop
                # Otherwise, retry with new version
    finally:
        conn.close()


# ============================================================
# Test Runner
# ============================================================

def run_test(name: str, worker_func: Callable, db_config: DatabaseConfig,
             num_threads: int = 10, iterations_per_thread: int = 10000):
    """Run a concurrent test with specified worker function"""

    print(f"\n{'='*60}")
    print(f"TEST: {name}")
    print(f"{'='*60}")
    print(f"Threads: {num_threads}")
    print(f"Iterations per thread: {iterations_per_thread}")
    print(f"Expected final count: {num_threads * iterations_per_thread}")
    print()

    # Reset counter
    reset_counter(db_config)

    # Run concurrent workers
    start_time = time.perf_counter()

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(worker_func, db_config, iterations_per_thread)
            for _ in range(num_threads)
        ]

        # Wait for all to complete
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Worker error: {e}")

    end_time = time.perf_counter()
    elapsed = end_time - start_time

    # Get final counter value
    final_value = get_counter_value(db_config)
    expected_value = num_threads * iterations_per_thread

    # Calculate throughput
    throughput = (num_threads * iterations_per_thread) / elapsed if elapsed > 0 else 0

    # Results
    print(f"Results:")
    print(f"  Final counter value: {final_value}")
    print(f"  Expected value: {expected_value}")
    print(f"  Lost updates: {expected_value - final_value}")
    print(f"  Elapsed time: {elapsed:.2f} seconds")
    print(f"  Throughput: {throughput:.2f} updates/second")

    if final_value == expected_value:
        print(f"  ✓ SUCCESS: No lost updates!")
    else:
        print(f"  ✗ FAILURE: Lost {expected_value - final_value} updates!")

    return {
        'name': name,
        'final_value': final_value,
        'expected_value': expected_value,
        'lost_updates': expected_value - final_value,
        'elapsed': elapsed,
        'throughput': throughput,
        'success': final_value == expected_value
    }


def main():
    """Run all tests"""

    # Database configuration
    db_config = DatabaseConfig(
        host="postgres",
        port=5432,
        database="counter_db",
        user="postgres",
        password="postgres"
    )

    print("\n" + "="*60)
    print("PostgreSQL Counter Implementation Tests")
    print("="*60)

    results = []

    # Test 1: Lost Update
    results.append(run_test(
        "1. Lost Update (NOT thread-safe)",
        lost_update_worker,
        db_config
    ))

    # Test 2: Serializable
    results.append(run_test(
        "2. Serializable Isolation Level",
        serializable_worker,
        db_config
    ))

    # Test 3: In-place Update
    results.append(run_test(
        "3. In-place Atomic Update",
        inplace_update_worker,
        db_config
    ))

    # Test 4: Row-level Locking
    results.append(run_test(
        "4. Row-level Locking (FOR UPDATE)",
        row_locking_worker,
        db_config
    ))

    # Test 5: Optimistic Locking
    results.append(run_test(
        "5. Optimistic Concurrency Control",
        optimistic_locking_worker,
        db_config
    ))

    # Summary
    print("\n" + "="*60)
    print("SUMMARY OF ALL TESTS")
    print("="*60)
    print(f"{'Test':<40} {'Result':<10} {'Time (s)':<12} {'Throughput (ops/s)':<20}")
    print("-"*60)

    for r in results:
        status = "✓ PASS" if r['success'] else "✗ FAIL"
        print(f"{r['name']:<40} {status:<10} {r['elapsed']:<12.2f} {r['throughput']:<20.2f}")

    print("="*60)


if __name__ == "__main__":
    main()

