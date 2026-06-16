#!/usr/bin/env python3
"""
Task 7 - Part II: Performance & Integrity Test
10 concurrent clients, each incrementing a likes counter 10_000 times.
Usage:
    python perf_test.py --write-concern 1
    python perf_test.py --write-concern majority
"""
import argparse
import time
import threading
from pymongo import MongoClient
from pymongo.write_concern import WriteConcern

MONGO_URI = "mongodb://mongo1:27017,mongo2:27018,mongo3:27019/?replicaSet=myReplicaSet"
DB_NAME = "task7"
COLLECTION = "likes"
COUNTER_KEY = "post_1"
NUM_CLIENTS = 10
INCREMENTS_PER_CLIENT = 10_000
EXPECTED_TOTAL = NUM_CLIENTS * INCREMENTS_PER_CLIENT  # 100_000


def increment_worker(write_concern, client_id: int, errors: list):
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=30_000)
        db = client[DB_NAME]
        col = db.get_collection(
            COLLECTION,
            write_concern=WriteConcern(w=write_concern)
        )
        for _ in range(INCREMENTS_PER_CLIENT):
            col.find_one_and_update(
                {"_id": COUNTER_KEY},
                {"$inc": {"likes": 1}},
                upsert=True
            )
        client.close()
        print(f"  [client-{client_id:02d}] done")
    except Exception as e:
        errors.append(f"client-{client_id}: {e}")
        print(f"  [client-{client_id:02d}] ERROR: {e}")


def run_test(write_concern):
    print(f"\n{'='*55}")
    print(f" writeConcern = {write_concern}")
    print(f"{'='*55}")

    # Setup: reset counter
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=30_000)
    db = client[DB_NAME]
    db[COLLECTION].delete_many({})
    db[COLLECTION].insert_one({"_id": COUNTER_KEY, "likes": 0})
    client.close()
    print(f"Counter reset to 0")

    errors = []
    threads = [
        threading.Thread(target=increment_worker, args=(write_concern, i, errors))
        for i in range(NUM_CLIENTS)
    ]

    print(f"Starting {NUM_CLIENTS} clients ({INCREMENTS_PER_CLIENT} increments each)...")
    start = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    elapsed = time.time() - start

    # Read final value
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=30_000)
    doc = client[DB_NAME][COLLECTION].find_one({"_id": COUNTER_KEY})
    final_value = doc["likes"] if doc else "NOT FOUND"
    client.close()

    print(f"\nTime elapsed : {elapsed:.2f}s")
    print(f"Final value  : {final_value}")
    print(f"Expected     : {EXPECTED_TOTAL}")
    print(f"Correct      : {final_value == EXPECTED_TOTAL}")
    if errors:
        print(f"Errors       : {len(errors)}")
        for e in errors:
            print(f"  {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-concern", "-w",
        default="majority",
        help='Write concern: 1 or majority (default: majority)'
    )
    args = parser.parse_args()

    wc = args.write_concern
    if wc.isdigit():
        wc = int(wc)

    run_test(wc)


if __name__ == "__main__":
    main()