"""
PostgreSQL counter for Web-counter application (Task 1 integration)
Uses in-place update for thread-safety
"""
import psycopg2
import os


class PostgresCounter:
    """
    PostgreSQL-based counter using in-place atomic update.
    Thread-safe and persistent.
    """

    def __init__(self, host="postgres", port=5432, database="counter_db",
                 user="postgres", password="postgres", user_id=1):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.user_id = user_id
        self._init_db()

    def _get_connection(self):
        """Create a new database connection"""
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def _init_db(self):
        """Initialize database table if needed"""
        conn = self._get_connection()
        try:
            cursor = conn.cursor()

            # Create table if not exists
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_counter (
                    user_id INTEGER PRIMARY KEY,
                    counter INTEGER NOT NULL DEFAULT 0,
                    version INTEGER NOT NULL DEFAULT 0
                )
            """)

            # Insert user if not exists
            cursor.execute("""
                INSERT INTO user_counter (user_id, counter, version)
                VALUES (%s, 0, 0)
                ON CONFLICT (user_id) DO NOTHING
            """, (self.user_id,))

            conn.commit()
        finally:
            conn.close()

    def increment(self) -> int:
        """
        Increment counter using atomic in-place update.
        Returns new counter value.
        """
        conn = self._get_connection()
        try:
            cursor = conn.cursor()

            # Atomic increment and return new value
            cursor.execute("""
                UPDATE user_counter 
                SET counter = counter + 1 
                WHERE user_id = %s
                RETURNING counter
            """, (self.user_id,))

            result = cursor.fetchone()
            conn.commit()

            return result[0] if result else 0
        finally:
            conn.close()

    def get(self) -> int:
        """Get current counter value"""
        conn = self._get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT counter FROM user_counter WHERE user_id = %s",
                (self.user_id,)
            )
            result = cursor.fetchone()
            return result[0] if result else 0
        finally:
            conn.close()

