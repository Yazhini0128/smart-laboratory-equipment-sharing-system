# Simulation / Software Demonstration

The repository includes a PC-runnable software demonstration of the core logic because Raspberry Pi 4 is not available as a standard Tinkercad component.

Run:

```bash
python src/main.py --demo
```

The demo shows:
- RFID authentication
- available-resource allocation
- mutex-protected state update
- FCFS queueing
- return handling
- next-student allocation
- invalid RFID indication

For a physical Raspberry Pi demonstration, connect the documented peripherals and replace/extend the hardware abstraction with the actual GPIO/RFID drivers.
