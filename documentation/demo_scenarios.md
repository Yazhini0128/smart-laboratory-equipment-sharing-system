# Demo Scenarios
## 1. Successful access
Student A scans RFID → UID is checked → availability checked → mutex-protected allocation → event recorded → intended servo/LCD feedback.
Expected: authorised access when equipment is available.

## 2. Conflict handling
Student B requests occupied equipment → joins FCFS queue → Student A returns equipment → state updated → next request considered.
Expected: fair FCFS handling.

## 3. Security breach
Unknown UID → authentication rejected → design calls for red LED and buzzer → denied attempt recorded.
Expected: access denied. Mark hardware alerts and audit encryption as verified only after testing.
