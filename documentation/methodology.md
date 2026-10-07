# Methodology
1. **Identification:** RC522 reads the RFID UID.
2. **Authentication:** application checks the UID against authorised student records.
3. **Validation:** check equipment availability; if occupied, enqueue the request using FCFS.
4. **Allocation:** protect shared allocation/database state with a mutex and record the event.
5. **Physical access:** servo unlocks the station and LCD shows the equipment ID.
6. **Completion:** after return, update status and check the waiting queue.

The mutex should protect shared state changes, not remain held while a student uses equipment or waits.
