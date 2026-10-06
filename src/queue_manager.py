from collections import deque

class WaitingQueue:
    def __init__(self):
        self.queue = deque()

    def add_student(self, student_id):
        self.queue.append(student_id)

    def next_student(self):
        return self.queue.popleft() if self.queue else None

    def position(self, student_id):
        try:
            return list(self.queue).index(student_id) + 1
        except ValueError:
            return None
