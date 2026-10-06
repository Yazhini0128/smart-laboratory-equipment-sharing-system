# Smart Laboratory Equipment Sharing System

Raspberry Pi based Smart Laboratory Equipment Sharing System implementing RFID authentication, resource allocation, mutual exclusion, synchronization, and FCFS queue management.

## Features
- RFID student authentication
- Equipment availability checking
- Mutex-protected resource allocation
- SQLite logging
- FCFS waiting queue
- Servo-based access control
- LCD, LED and buzzer status indication

## OS Concepts
Process Management • Mutual Exclusion • Critical Section • Resource Allocation • Synchronization • FCFS Queue Management

## Main Hardware
Raspberry Pi 4, RC522 RFID reader, RFID cards/tags, 16x2 I2C LCD, SG90 servos, LEDs, active buzzer, resistors, level converter, breadboard and jumper wires.

## Repository Structure
- `src/` Python source
- `database/` SQLite schema
- `hardware/` components and pin configuration
- `documentation/` architecture and methodology
- `simulation/` simulation notes
- `testing/` test cases/results
- `screenshots/` final demo images

> Academic prototype. Hardware-specific GPIO/RFID integration should be verified on the actual Raspberry Pi.
