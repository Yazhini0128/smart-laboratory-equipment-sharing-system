"""Hardware abstraction.

The project runs in DEMO mode on a normal PC. On Raspberry Pi, the same
application can be connected to GPIO/LCD/RFID/servo drivers through this
module. Hardware calls are intentionally isolated from OS/resource logic.
"""
class HardwareInterface:
    def __init__(self, demo=True):
        self.demo = demo

    def lcd(self, message):
        print(f"[LCD] {message}")

    def green(self):
        print("[GREEN LED] ON")

    def red_buzzer(self):
        print("[RED LED] ON + [BUZZER] ON")

    def unlock(self):
        print("[SERVO] UNLOCK")

    def lock(self):
        print("[SERVO] LOCK")
