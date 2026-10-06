# Test Cases

| ID | Test | Expected Result |
|---|---|---|
| TC01 | Valid RFID | Student authenticated |
| TC02 | Invalid RFID | Red LED + buzzer |
| TC03 | Equipment available | Equipment allocated |
| TC04 | Equipment unavailable | Student added to FCFS queue |
| TC05 | Equipment returned | Database updated |
| TC06 | Waiting students exist | Next student selected |
| TC07 | Multiple requests | Mutex prevents conflicting updates |
