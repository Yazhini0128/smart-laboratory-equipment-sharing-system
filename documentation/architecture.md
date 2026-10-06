# System Architecture

START -> RFID Scan -> Authenticate Student

Authentication successful?
NO -> Red LED + Buzzer -> END
YES -> Acquire Mutex -> Check Equipment Availability

Available?
YES -> Allocate -> Update SQLite -> Release Mutex -> Unlock Servo
-> LCD Allocation Message -> Green LED -> Student Uses Equipment
-> Student Returns -> Update Database -> Check Waiting Queue

NO -> Add Student to FCFS Queue -> Display Queue Position
-> Wait for Return -> Check Waiting Queue

Students Waiting?
NO -> END
YES -> Select Next Student -> Acquire Mutex -> Allocate
-> Update Database -> Release Mutex -> Unlock Servo -> LCD -> END
