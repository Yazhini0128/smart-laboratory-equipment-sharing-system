from hardware import HardwareInterface
_display = HardwareInterface()

def display(message):
    _display.lcd(message)
