#!/usr/bin/env python3
"""
Task 8 - Part 3: Performance & Integrity Test
10 concurrent clients, each incrementing a likes counter 10_000 times.

Usage:
    python perf_test.py --consistency one
    python perf_test.py --consistency quorum
"""
import argparse
import time
import threading
from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement

CASSANDRA_HOSTS = ["127.0.0.1"]
CASSANDRA_PORT = 9042

KEYSPACE = "task8_rf3"
TABLE = "likes"
COUNTER_KEY = "post_1"

NUM_CLIENTS = 10
INCREMENTS_PER_CLIENT = 10_000
EXPECTED_TOTAL = NUM_CLIENTS * INCREMENTS_PER_CLIENT  # 100_000

CONSISTENCY_MAP = {
    "one": ConsistencyLevel.ONE,
    "quorum": ConsistencyLevel.QUORUM,
}


def setup_schema() -> None:
    cluster = Cluster(CASSANDRA_HOSTS, port=CASSANDRA_PORT)
    session = cluster.connect()

    # Create keyspace with RF=3
    session.execute(f"""
        CREATE KEYSPACE IF NOT EXISTS {KEYSPACE}
        WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': 3}}
    """)
    session.set_keyspace(KEYSPACE)

    # Counter tables cannot be mixed with non-counter columns (except PK)
    session.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE} (
            post_id  text PRIMARY KEY,
            likes    counter
        )
    """)

    # Truncate to reset counter (counters cannot be set to an arbitrary value)
    session.execute(f"TRUNCATE {TABLE}")
    cluster.shutdown()
    print("Schema setup done, counter reset to 0.")


def increment_worker(
    consistency_level: int, client_id: int, errors: list
) -> None:
    try:
        cluster = Cluster(CASSANDRA_HOSTS, port=CASSANDRA_PORT)
        session = cluster.connect(KEYSPACE)

        stmt = SimpleStatement(
            f"UPDATE {TABLE} SET likes = likes + 1 WHERE post_id = '{COUNTER_KEY}'",
            consistency_level=consistency_level,
        )

        for _ in range(INCREMENTS_PER_CLIENT):
            session.execute(stmt)

        cluster.shutdown()
        print(f"  [client-{client_id:02d}] done")
    except Exception as exc:
        errors.append(f"client-{client_id}: {exc}")
        print(f"  [client-{client_id:02d}] ERROR: {exc}")


def run_test(consistency_name: str) -> None:
    consistency_level = CONSISTENCY_MAP[consistency_name.lower()]

    print(f"\n{'=' * 55}")
    print(f" Consistency Level = {consistency_name.upper()}")
    print(f"{'=' * 55}")

    setup_schema()

    errors: list[str] = []
    threads = [
        threading.Thread(
            target=increment_worker, args=(consistency_level, i, errors)
        )
        for i in range(NUM_CLIENTS)
    ]

    print(
        f"Starting {NUM_CLIENTS} clients "
        f"({INCREMENTS_PER_CLIENT} increments each)..."
    )
    start = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    elapsed = time.time() - start

    # Read final value
    cluster = Cluster(CASSANDRA_HOSTS, port=CASSANDRA_PORT)
    session = cluster.connect(KEYSPACE)
    row = session.execute(
        f"SELECT likes FROM {TABLE} WHERE post_id = '{COUNTER_KEY}'"
    ).one()
    final_value = row.likes if row else "NOT FOUND"
    cluster.shutdown()

    print(f"\nTime elapsed : {elapsed:.2f}s")
    print(f"Final value  : {final_value}")
    print(f"Expected     : {EXPECTED_TOTAL}")
    print(f"Correct      : {final_value == EXPECTED_TOTAL}")
    if errors:
        print(f"Errors       : {len(errors)}")
        for err in errors:
            print(f"  {err}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Cassandra counter performance & integrity test"
    )
    parser.add_argument(
        "--consistency",
        "-c",
        default="quorum",
        choices=["one", "quorum"],
        help="Consistency level: one or quorum (default: quorum)",
    )
    args = parser.parse_args()
    run_test(args.consistency)


if __name__ == "__main__":
    main()

