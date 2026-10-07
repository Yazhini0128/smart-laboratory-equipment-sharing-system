# Software Architecture
Review each responsibility against the actual source before claiming it is implemented:
- `main.py`: application entry point/workflow.
- `auth.py`: UID authorisation check.
- `database.py`: SQLite operations.
- `queue_manager.py`: FCFS queue.
- `resource_manager.py`: availability, allocation and locking.
- `rfid.py`: RFID integration or demo abstraction.
- `lcd.py`: LCD output abstraction.
- `servo.py`: servo/lock abstraction.
- `config.py`, `hardware.py`: configuration/hardware abstraction if present.

Document only the demo command that is actually supported by `main.py`. A software demo is not proof of physical hardware operation.
