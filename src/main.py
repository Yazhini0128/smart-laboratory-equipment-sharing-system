"""Interactive software prototype for the Smart Laboratory Equipment Sharing System.

Run from the repository root:
    python src/main.py
or:
    python src/main.py --demo
"""
import argparse
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from database import (
    initialize_database, seed_demo_data, get_equipment,
    add_waiting_request, get_queue, pop_next_waiting
)
from auth import authenticate_student
from resource_manager import ResourceManager
from hardware import HardwareInterface

def allocate_flow(manager, hw, student_id, equipment_id):
    equipment = get_equipment(equipment_id)
    if not equipment:
        hw.lcd("Equipment not found")
        return False
    if manager.allocate(equipment_id, student_id):
        hw.unlock()
        hw.lcd(f"Allocated: {equipment[1]}")
        hw.green()
        return True
    return False

def request_equipment(manager, hw, uid, equipment_id):
    student = authenticate_student(uid)
    if not student:
        hw.red_buzzer()
        hw.lcd("Authentication Failed")
        return "DENIED"

    student_id, name, _ = student
    hw.lcd(f"Welcome {name}")
    if allocate_flow(manager, hw, student_id, equipment_id):
        return "ALLOCATED"

    queue_id = add_waiting_request(student_id, equipment_id)
    queue = get_queue(equipment_id)
    position = next((r[3] for r in queue if r[0] == queue_id), None)
    hw.lcd(f"Queue Position: {position}")
    return "QUEUED"

def return_equipment(manager, hw, equipment_id):
    if not manager.release(equipment_id):
        hw.lcd("Return rejected")
        return None

    hw.lcd("Equipment Returned")
    next_row = pop_next_waiting(equipment_id)
    if not next_row:
        hw.lcd("No Students Waiting")
        hw.lock()
        return None

    next_student_id = next_row[1]
    if allocate_flow(manager, hw, next_student_id, equipment_id):
        return next_student_id
    return None

def demo():
    initialize_database()
    seed_demo_data()
    manager = ResourceManager()
    hw = HardwareInterface(demo=True)

    print("\n=== SMART LAB EQUIPMENT SHARING SYSTEM ===")
    print("DEMO 1: Student 1 requests equipment 1")
    print(request_equipment(manager, hw, "DEMO_UID_001", 1))

    print("\nDEMO 2: Student 2 requests the same equipment")
    print(request_equipment(manager, hw, "DEMO_UID_002", 1))

    print("\nDEMO 3: Student 1 returns equipment")
    print("Next allocated student:", return_equipment(manager, hw, 1))

    print("\nDEMO 4: Invalid RFID")
    print(request_equipment(manager, hw, "INVALID_UID", 2))

    print("\nFinal queue:", get_queue(1))
    print("Demo complete.")

def interactive():
    initialize_database()
    seed_demo_data()
    manager = ResourceManager()
    hw = HardwareInterface(demo=True)

    while True:
        print("\n1. Request equipment\n2. Return equipment\n3. Show equipment\n4. Show queue\n5. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            uid = input("RFID UID: ")
            equipment_id = int(input("Equipment ID (1/2): "))
            print("Result:", request_equipment(manager, hw, uid, equipment_id))
        elif choice == "2":
            equipment_id = int(input("Equipment ID (1/2): "))
            print("Next allocation:", return_equipment(manager, hw, equipment_id))
        elif choice == "3":
            for eid in (1, 2):
                print(get_equipment(eid))
        elif choice == "4":
            eid = int(input("Equipment ID: "))
            print(get_queue(eid))
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="run automatic software demo")
    args = parser.parse_args()
    demo() if args.demo else interactive()
