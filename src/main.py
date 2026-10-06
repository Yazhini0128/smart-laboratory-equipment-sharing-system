from database import initialize_database
from auth import authenticate_student
from queue_manager import WaitingQueue

def main():
    print("Smart Laboratory Equipment Sharing System")
    initialize_database()
    print("System initialized.")

if __name__ == "__main__":
    main()
