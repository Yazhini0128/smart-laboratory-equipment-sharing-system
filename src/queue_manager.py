"""Thread-safe FCFS waiting queue."""
from collections import deque
from threading import Lock

class WaitingQueue:
    def __init__(self):
        self._queue = deque()
        self._lock = Lock()

    def add_student(self, student_id):
        with self._lock:
            if student_id not in self._queue:
                self._queue.append(student_id)
            return self.position_unlocked(student_id)

    def next_student(self):
        with self._lock:
            return self._queue.popleft() if self._queue else None

    def position(self, student_id):
        with self._lock:
            return self.position_unlocked(student_id)

    def position_unlocked(self, student_id):
        try:
            return list(self._queue).index(student_id) + 1
        except ValueError:
            return None

    def __len__(self):
        with self._lock:
            return len(self._queue)
