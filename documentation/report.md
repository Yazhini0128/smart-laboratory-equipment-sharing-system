# Smart Laboratory Equipment Sharing System — Report Draft

## Abstract
A Raspberry Pi based laboratory equipment sharing prototype that combines RFID authentication, SQLite resource tracking, mutex-protected allocation and FCFS waiting-queue management.

## Problem Statement
Shared laboratory equipment can be difficult to track manually, leading to conflicts, unavailable resources and poor visibility of who is using equipment.

## Objectives
- Authenticate students using RFID.
- Track equipment availability.
- Prevent conflicting allocations using mutual exclusion.
- Maintain an FCFS waiting queue.
- Record allocation and return transactions.
- Provide status feedback through LCD, LEDs, buzzer and servo access control.

## Proposed System
The application separates hardware I/O from resource-management logic. RFID identifies the student, the resource manager enters a mutex-protected critical section to check and update equipment state, and SQLite stores persistent records.

## OS Concepts
### Mutual Exclusion
A `threading.Lock` protects the shared allocation operation.

### Critical Section
The availability check and database state update form the critical section.

### Resource Allocation
An equipment item is allocated only when its database status is `AVAILABLE`.

### Synchronization
Return events trigger a check of the waiting queue and allow the next waiting student to be selected.

### FCFS
Students waiting for an unavailable resource are ordered by arrival.

### Process/Application Modules
Authentication, persistence, queue management, resource management and hardware abstraction are separated into modules.

## Testing
The repository contains functional test cases for valid/invalid RFID, allocation, queueing, return and mutex behavior. Hardware results must be updated after physical verification.

## Limitations
The submitted software can run in demo mode on a normal computer. Raspberry Pi GPIO, RC522 and peripheral behavior requires physical hardware verification.

## Future Enhancements
- Web dashboard
- Faculty/admin authentication
- Multiple concurrent resource requests
- Audit reports
- Notifications
- Improved hardware fault handling
