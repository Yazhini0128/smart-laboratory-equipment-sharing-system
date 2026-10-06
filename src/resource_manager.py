"""Mutex-protected resource allocation."""
from threading import Lock
from database import get_equipment, set_equipment_status

class ResourceManager:
    def __init__(self):
        self.mutex = Lock()

    def allocate(self, equipment_id, student_id):
        # Critical section: availability check + state update.
        with self.mutex:
            equipment = get_equipment(equipment_id)
            if equipment is None or equipment[2] != "AVAILABLE":
                return False
            set_equipment_status(equipment_id, "ALLOCATED", student_id)
            return True

    def release(self, equipment_id):
        # Critical section: shared resource state update.
        with self.mutex:
            equipment = get_equipment(equipment_id)
            if equipment is None or equipment[2] != "ALLOCATED":
                return False
            set_equipment_status(equipment_id, "AVAILABLE")
            return True
