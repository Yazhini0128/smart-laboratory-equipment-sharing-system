"""Central configuration for the Smart Laboratory Equipment Sharing System."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = PROJECT_ROOT / "database" / "lab_equipment.db"

AUTHORIZED_UIDS = {
    "DEMO_UID_001": 1,
    "DEMO_UID_002": 2,
}

LCD_ADDRESS = 0x27
SERVO_1_GPIO = 17
SERVO_2_GPIO = 27
RFID_SS_GPIO = 8
RFID_RST_GPIO = 25
