import argparse
from flask import Flask, jsonify, request
from counter_inmemory import InMemoryCounter
from counter_file import FileCounter
from counter_postgres import PostgresCounter
from counter_hazelcast import HazelcastCounter

app = Flask(__name__)
counter = None


@app.route("/inc", methods=["POST", "GET"])
def inc():
    """Increment the counter"""
    new = counter.increment()
    return jsonify({"value": new}), 200


@app.route("/count", methods=["GET"])
def count():
    """Return current counter value"""
    return jsonify({"value": counter.get()}), 200


@app.route("/reset", methods=["POST"])
def reset():
    """Reset counter to 0 (useful for testing)"""
    global counter
    if isinstance(counter, InMemoryCounter):
        counter = InMemoryCounter()
    elif isinstance(counter, FileCounter):
        import os
        file_path = counter.file_path
        if os.path.exists(file_path):
            os.remove(file_path)
        counter = FileCounter(file_path=file_path)
    elif isinstance(counter, HazelcastCounter):
        counter.reset()
    else:
        counter.reset()
    return jsonify({"message": "Counter reset", "value": counter.get()}), 200


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend", choices=["inmemory", "file", "postgres", "hazelcast"], default="inmemory")
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--file", default="/data/counter.txt")
    args = parser.parse_args()

    global counter
    if args.backend == "inmemory":
        print(f"Using in-memory backend")
        counter = InMemoryCounter()
    elif args.backend == "file":
        print(f"Using file backend (file={args.file})")
        counter = FileCounter(file_path=args.file)
    elif args.backend == "postgres":
        print(f"Using PostgreSQL backend (atomic in-place update)")
        counter = PostgresCounter()
    elif args.backend == "hazelcast":
        print(f"Using Hazelcast backend (CP Subsystem with IAtomicLong)")
        counter = HazelcastCounter()

    print(f"Starting server on port {args.port}")
    # threaded=True to allow concurrent requests
    app.run(host="0.0.0.0", port=args.port, threaded=True)


if __name__ == "__main__":
    main()

