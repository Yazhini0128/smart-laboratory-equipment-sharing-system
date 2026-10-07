# Operating System Concepts
- **Process/request management:** each RFID request is handled as an incoming application task.
- **Scheduling:** requests are handled using the chosen application policy.
- **Mutual exclusion:** a mutex protects shared equipment state from conflicting updates.
- **Resource allocation:** allocate only if the item is available.
- **Synchronization:** keep resource state and database updates consistent.
- **FCFS queue:** waiting requests are served in first-come, first-served order.
- **Alert handling:** the design calls for a buzzer/LED response after an unauthorised scan.

These are application-level demonstrations; do not claim kernel-level Linux scheduling was modified. Describe alerts as application-triggered unless actual interrupt handling exists.
