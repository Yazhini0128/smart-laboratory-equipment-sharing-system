# Test Results

| ID | Test | Expected | Software Demo |
|---|---|---|---|
| TC01 | Valid RFID | Authenticated | PASS |
| TC02 | Invalid RFID | Red LED + buzzer | PASS |
| TC03 | Available equipment | Allocate + DB update | PASS |
| TC04 | Unavailable equipment | FCFS queue | PASS |
| TC05 | Equipment returned | Mark available | PASS |
| TC06 | Waiting student exists | Next student allocated | PASS |
| TC07 | Mutex-protected allocation | Conflicting state update prevented | PASS (logic-level) |

**Hardware verification:** Pending until the Raspberry Pi, RC522, LCD, servo, LEDs and buzzer are physically tested. Do not represent hardware results as completed unless verified.
