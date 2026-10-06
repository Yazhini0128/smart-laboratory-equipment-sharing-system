# Test Cases

| ID | Input/Action | Expected Result |
|---|---|---|
| TC01 | `DEMO_UID_001` requests available equipment | Student authenticated and equipment allocated |
| TC02 | `INVALID_UID` requests equipment | Request rejected; red LED/buzzer indication |
| TC03 | Student 1 requests equipment 1 | Equipment status becomes ALLOCATED |
| TC04 | Student 2 requests occupied equipment 1 | Student enters FCFS queue |
| TC05 | Current user returns equipment 1 | Equipment becomes AVAILABLE |
| TC06 | Queue contains Student 2 | Student 2 receives next allocation |
| TC07 | Concurrent allocation attempts | Mutex serializes the critical section |
