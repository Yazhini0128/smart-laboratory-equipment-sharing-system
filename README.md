# Smart Laboratory Equipment Sharing System

A Raspberry Pi based Smart Laboratory Equipment Sharing System implementing RFID authentication, mutex-protected resource allocation, SQLite persistence, synchronization and FCFS queue management.

## Problem
Laboratory equipment is often shared by many students. Manual allocation can cause conflicts, unclear ownership and inefficient waiting.

## Solution
The system authenticates students using RFID, checks equipment availability, protects shared state with a mutex, records allocations in SQLite, controls access through a servo and manages unavailable requests using an FCFS waiting queue.

## Core Features
- RFID authentication
- Equipment availability tracking
- Mutex / critical-section protection
- SQLite transaction logging
- FCFS waiting queue
- Return and next-student allocation
- LCD / LED / buzzer / servo hardware abstraction
- PC software demo for logic verification

## OS Concepts
- Mutual Exclusion
- Critical Section
- Resource Allocation
- Synchronization
- FCFS Queue Management
- Process/application modularization

## Hardware
Raspberry Pi 4, RC522/MFRC522 RFID reader, MIFARE tags, 16x2 I2C LCD, SG90 servos, LEDs, active buzzer, 220 ohm resistors, bidirectional level converter, breadboard, jumper wires and regulated 5V supply.

See `hardware/pin_configuration.md` and `hardware/components_list.md`.

## Run the software demo
No third-party package is required for demo mode.

From the repository root:

```bash
python src/main.py --demo
```

The demo automatically demonstrates:
1. Valid RFID authentication.
2. Allocation of an available equipment item.
3. A second student joining the FCFS queue.
4. Return of the equipment.
5. Automatic allocation to the next waiting student.
6. Invalid RFID rejection.

Interactive mode:

```bash
python src/main.py
```

## Raspberry Pi mode
Install the packages in `requirements.txt` on the Raspberry Pi and connect the hardware according to the documented pin map. The hardware drivers are intentionally isolated from the resource-management logic so the OS concepts can be tested independently.

## Database
SQLite tables:
- `students`
- `equipment`
- `waiting_queue`
- `transactions`

The database is created automatically in `database/lab_equipment.db` when the application starts.

## Architecture
See `documentation/architecture.md`.

## Testing
Software test cases and results are in `testing/`. The automated demo validates the core application logic. Physical hardware results remain pending until tested on the actual Raspberry Pi.

## Simulation
See `simulation/simulation_notes.md`. A PC software demo is included because the exact Raspberry Pi 4 hardware environment is not assumed to be available in browser simulators.

## Repository Structure
```text
database/       SQLite schema
documentation/  architecture, methodology, OS concepts, report draft
hardware/       components and GPIO pin map
simulation/     simulation/demo notes
src/            Python implementation
testing/        test cases/results
presentation/   presentation placeholder
report/         final report placeholder
config/         demo configuration
screenshots/    evidence placeholder
```

## Academic Note
This repository distinguishes between **software-verified behavior** and **physical hardware verification**. Hardware-specific claims should only be marked complete after testing on the Raspberry Pi.

## Team
Add the final team-member names, guide and institution details before submission if required.

## License
This repository is intended for academic/project submission.
