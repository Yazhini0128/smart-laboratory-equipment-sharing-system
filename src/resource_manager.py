import threading

resource_mutex = threading.Lock()

def allocate_equipment(equipment_id):
    with resource_mutex:
        print(f"Equipment {equipment_id} allocated safely.")

def release_equipment(equipment_id):
    with resource_mutex:
        print(f"Equipment {equipment_id} released.")
