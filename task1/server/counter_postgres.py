import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Optional
import os


class PostgresCounter:
    """PostgreSQL-backed counter using atomic in-place updates."""

    def __init__(self, db_config: Optional[dict] = None):
        """
        Initialize PostgreSQL counter.

        Args:
            db_config: Database configuration dict with keys:
                      host, port, database, user, password
        """
        if db_config is None:
            db_config = {
                'host': os.getenv('POSTGRES_HOST', 'localhost'),
                'port': int(os.getenv('POSTGRES_PORT', 5432)),
                'database': os.getenv('POSTGRES_DB', 'counter_db'),
                'user': os.getenv('POSTGRES_USER', 'postgres'),
                'password': os.getenv('POSTGRES_PASSWORD', 'postgres')
            }

        self.db_config = db_config
        self._init_database()

    def _get_connection(self):
        """Create a new database connection."""
        return psycopg2.connect(**self.db_config)

    def _init_database(self):
        """Initialize database table if it doesn't exist."""
        conn = self._get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS web_counter (
                        counter_id INTEGER PRIMARY KEY,
                        counter_value BIGINT NOT NULL DEFAULT 0
                    )
                """)

                # Insert default counter if not exists
                cursor.execute("""
                    INSERT INTO web_counter (counter_id, counter_value)
                    VALUES (1, 0)
                    ON CONFLICT (counter_id) DO NOTHING
                """)
                conn.commit()
        except Exception as e:
            conn.rollback()
            raise
        finally:
            conn.close()

    def increment(self) -> int:
        """
        Atomically increment counter and return new value.
        Uses in-place update for best performance.

        Returns:
            New counter value after increment
        """
        conn = self._get_connection()
        try:
            with conn.cursor() as cursor:
                # Atomic in-place update - fastest method from Task 2
                cursor.execute("""
                    UPDATE web_counter
                    SET counter_value = counter_value + 1
                    WHERE counter_id = 1
                    RETURNING counter_value
                """)
                result = cursor.fetchone()
                conn.commit()
                return result[0] if result else 0
        except Exception as e:
            conn.rollback()
            raise
        finally:
            conn.close()

    def get(self) -> int:
        """
        Get current counter value.

        Returns:
            Current counter value
        """
        conn = self._get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT counter_value FROM web_counter WHERE counter_id = 1"
                )
                result = cursor.fetchone()
                return result[0] if result else 0
        except Exception as e:
            raise
        finally:
            conn.close()

    def reset(self) -> None:
        """Reset counter to 0."""
        conn = self._get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE web_counter SET counter_value = 0 WHERE counter_id = 1"
                )
                conn.commit()
        except Exception as e:
            conn.rollback()
            raise
        finally:
            conn.close()
