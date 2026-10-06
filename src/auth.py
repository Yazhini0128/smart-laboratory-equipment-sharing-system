"""RFID authentication logic."""
from database import get_student_by_uid

def normalize_uid(uid):
    return str(uid).strip().upper().replace(" ", "")

def authenticate_student(uid):
    return get_student_by_uid(normalize_uid(uid))
