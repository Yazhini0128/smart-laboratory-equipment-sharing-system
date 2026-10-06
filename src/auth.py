AUTHORIZED_UIDS = {
    "DEMO_UID_001": "Student 1",
    "DEMO_UID_002": "Student 2",
}

def authenticate_student(uid):
    return AUTHORIZED_UIDS.get(uid)
