# Methodology

1. Student presents an RFID card.
2. UID is normalized and authenticated against registered students.
3. Invalid authentication produces a red LED/buzzer indication.
4. A valid request enters the resource manager.
5. A mutex protects the availability check and allocation update.
6. SQLite records the allocation.
7. Hardware feedback opens the equipment enclosure and displays status.
8. If unavailable, the request is placed in an FCFS queue.
9. On return, the resource is marked available.
10. The next waiting student is selected and allocated.
11. Transaction records provide an audit trail.
