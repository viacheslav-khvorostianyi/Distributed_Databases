import threading
class InMemoryCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    def increment(self):
        with self.lock:
            self.value += 1
            return self.value
    def get(self):
        with self.lock:
            return self.value
