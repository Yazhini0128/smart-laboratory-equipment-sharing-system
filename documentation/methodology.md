# Methodology

1. Student scans RFID.
2. System authenticates the UID.
3. Mutex protects shared allocation state.
4. Equipment availability is checked.
5. Available equipment is allocated and logged in SQLite.
6. Servo controls equipment access.
7. LCD, LEDs and buzzer show status.
8. If unavailable, the student joins the FCFS queue.
9. On return, the database is updated.
10. The next waiting student is selected.
