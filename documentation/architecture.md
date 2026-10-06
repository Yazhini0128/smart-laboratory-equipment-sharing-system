# System Architecture

```text
START
  |
Student scans RFID
  |
Authenticate Student
  |---- NO ----> Red LED + Buzzer ----> END
  |
 YES
  |
Acquire Mutex
  |
Check Equipment Availability
  |---- NO ----> Add to FCFS Queue -> Display Queue Position
  |                              -> Wait for Return -> Check Queue
  |---- YES
  |
Allocate Equipment
  |
Update SQLite Database
  |
Release Mutex
  |
Unlock Servo + LCD + Green LED
  |
Student Uses Equipment
  |
Student Returns Equipment
  |
Update Database
  |
Check Waiting Queue
  |---- NO ----> END
  |
 YES
  |
Select Next Student
  |
Acquire Mutex -> Allocate -> Update DB -> Release Mutex
  |
Unlock Servo + LCD
  |
END
```

The mutex is not held while a student physically uses or waits for equipment. It protects only the shared resource state update.
