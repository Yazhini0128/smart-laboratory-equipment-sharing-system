"""SQLite persistence layer."""
import sqlite3
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DB_NAME = BASE_DIR / "database" / "lab_equipment.db"
SCHEMA = BASE_DIR / "database" / "schema.sql"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_database():
    DB_NAME.parent.mkdir(parents=True, exist_ok=True)
    with get_connection() as conn:
        conn.executescript(SCHEMA.read_text(encoding="utf-8"))

def seed_demo_data():
    with get_connection() as conn:
        conn.execute(
            "INSERT OR IGNORE INTO students(student_id,name,rfid_uid) VALUES(1,?,?)",
            ("Student 1", "DEMO_UID_001"),
        )
        conn.execute(
            "INSERT OR IGNORE INTO students(student_id,name,rfid_uid) VALUES(2,?,?)",
            ("Student 2", "DEMO_UID_002"),
        )
        conn.execute(
            "INSERT OR IGNORE INTO equipment(equipment_id,equipment_name,status) VALUES(1,?,?)",
            ("Digital Multimeter", "AVAILABLE"),
        )
        conn.execute(
            "INSERT OR IGNORE INTO equipment(equipment_id,equipment_name,status) VALUES(2,?,?)",
            ("Oscilloscope", "AVAILABLE"),
        )

def get_student_by_uid(uid):
    with get_connection() as conn:
        return conn.execute(
            "SELECT student_id,name,rfid_uid FROM students WHERE rfid_uid=?",
            (uid.strip().upper(),),
        ).fetchone()

def get_equipment(equipment_id):
    with get_connection() as conn:
        return conn.execute(
            "SELECT equipment_id,equipment_name,status FROM equipment WHERE equipment_id=?",
            (equipment_id,),
        ).fetchone()

def set_equipment_status(equipment_id, status, student_id=None):
    with get_connection() as conn:
        conn.execute(
            "UPDATE equipment SET status=? WHERE equipment_id=?",
            (status, equipment_id),
        )
        if status == "ALLOCATED" and student_id is not None:
            conn.execute(
                "INSERT INTO transactions(student_id,equipment_id,action) VALUES(?,?,?)",
                (student_id, equipment_id, "ALLOCATED"),
            )
        elif status == "AVAILABLE":
            conn.execute(
                "INSERT INTO transactions(equipment_id,action) VALUES(?,?)",
                (equipment_id, "RETURNED"),
            )

def add_waiting_request(student_id, equipment_id):
    with get_connection() as conn:
        existing = conn.execute(
            "SELECT queue_id FROM waiting_queue WHERE student_id=? AND equipment_id=?",
            (student_id, equipment_id),
        ).fetchone()
        if existing:
            return existing[0]
        pos = conn.execute(
            "SELECT COALESCE(MAX(position),0)+1 FROM waiting_queue WHERE equipment_id=?",
            (equipment_id,),
        ).fetchone()[0]
        cur = conn.execute(
            "INSERT INTO waiting_queue(student_id,equipment_id,position) VALUES(?,?,?)",
            (student_id, equipment_id, pos),
        )
        return cur.lastrowid

def get_queue(equipment_id):
    with get_connection() as conn:
        return conn.execute(
            "SELECT queue_id,student_id,equipment_id,position FROM waiting_queue "
            "WHERE equipment_id=? ORDER BY position",
            (equipment_id,),
        ).fetchall()

def pop_next_waiting(equipment_id):
    with get_connection() as conn:
        row = conn.execute(
            "SELECT queue_id,student_id,equipment_id,position FROM waiting_queue "
            "WHERE equipment_id=? ORDER BY position LIMIT 1",
            (equipment_id,),
        ).fetchone()
        if row:
            conn.execute("DELETE FROM waiting_queue WHERE queue_id=?", (row[0],))
            conn.execute(
                "UPDATE waiting_queue SET position=position-1 "
                "WHERE equipment_id=? AND position>?",
                (equipment_id, row[3]),
            )
        return row

def get_transactions():
    with get_connection() as conn:
        return conn.execute(
            "SELECT transaction_id,student_id,equipment_id,action,timestamp "
            "FROM transactions ORDER BY transaction_id"
        ).fetchall()
