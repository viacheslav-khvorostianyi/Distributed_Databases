import concurrent.futures
import time
from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "password123")


def increment_likes(client_id, iterations=10000):
    """Інкрементує лайки для конкретного клієнта"""
    driver = GraphDatabase.driver(URI, auth=AUTH)

    with driver.session() as session:
        for i in range(iterations):
            session.run(
                """
                MATCH (i:Item {item_id: 'ITEM001'})
                SET i.likes = i.likes + 1
                RETURN i.likes
                """,
                {}
            )

    driver.close()
    print(f"Client {client_id} completed {iterations} increments")
    return client_id


def main():
    num_clients = 10
    iterations_per_client = 10000
    expected_total = num_clients * iterations_per_client
    driver = GraphDatabase.driver(URI, auth=AUTH)
    with driver.session() as session:
        session.run(
            """
            MATCH (i:Item {item_id: 'ITEM001'})
            SET i.likes = 0
            RETURN i.likes
            """
        )
    driver.close()
    print("Initialized likes to 0")

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_clients) as executor:
        futures = [
            executor.submit(increment_likes, client_id, iterations_per_client)
            for client_id in range(1, num_clients + 1)
        ]

        concurrent.futures.wait(futures)

    end_time = time.time()
    execution_time = end_time - start_time

    # Перевірка фінального значення
    driver = GraphDatabase.driver(URI, auth=AUTH)
    with driver.session() as session:
        result = session.run(
            "MATCH (i:Item {item_id: 'ITEM001'}) RETURN i.likes AS likes"
        )
        final_likes = result.single()["likes"]

    driver.close()

    print(f"\n{'=' * 60}")
    print(f"Performance Test Results:")
    print(f"{'=' * 60}")
    print(f"Expected likes: {expected_total}")
    print(f"Final likes: {final_likes}")
    print(f"Difference: {expected_total - final_likes}")
    print(f"Execution time: {execution_time:.2f} seconds")
    print(f"Operations per second: {(num_clients * iterations_per_client) / execution_time:.2f}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()