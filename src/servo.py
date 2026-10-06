from hardware import HardwareInterface
_hw = HardwareInterface()

def unlock_servo():
    _hw.unlock()

def lock_servo():
    _hw.lock()
