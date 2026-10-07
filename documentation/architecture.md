# System Architecture
The supplied PPT describes four layers:
1. **User:** student scans an RFID card and sends a UID request.
2. **Processing:** Raspberry Pi 4/Linux validates the UID and coordinates scheduling, mutex use, and resource allocation.
3. **Data:** SQLite stores records; the presentation specifies AES-encrypted audit logs.
4. **Action:** servo controls the lock, LCD displays equipment status, and LED/buzzer provide feedback.

Logical path: Student → RFID card → RC522 → Raspberry Pi application → authentication/availability → mutex-protected allocation and database update → servo/LCD/LED/buzzer.

When equipment is occupied, a request joins the FCFS queue. After return, equipment state is updated and the next waiting request is considered. This describes the intended design; physical behaviour must be verified on the actual hardware.
