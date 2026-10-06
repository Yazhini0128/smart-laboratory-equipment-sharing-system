"""RFID reader abstraction with a safe demo fallback."""
def read_uid():
    return input("Scan RFID (demo UID): ").strip()

class RFIDReader:
    def read(self):
        return read_uid()
