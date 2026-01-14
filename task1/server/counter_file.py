import os
import threading


class FileCounter:
    """
    Simple file-based counter.
    Uses a text file + threading.Lock for thread safety.
    Much simpler than SQLite!
    """
    def __init__(self, file_path: str = "/data/counter.txt"):
        self.file_path = file_path
        self._lock = threading.Lock()

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Initialize file with 0 if it doesn't exist
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                f.write('0')

    def increment(self) -> int:
        with self._lock:
            # Read current value
            with open(self.file_path, 'r') as f:
                value = int(f.read().strip() or '0')

            # Increment
            value += 1

            # Write new value
            with open(self.file_path, 'w') as f:
                f.write(str(value))

            return value

    def get(self) -> int:
        with self._lock:
            with open(self.file_path, 'r') as f:
                return int(f.read().strip() or '0')

