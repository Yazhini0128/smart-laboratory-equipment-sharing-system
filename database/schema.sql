CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rfid_uid TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS equipment (
    equipment_id INTEGER PRIMARY KEY,
    equipment_name TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('AVAILABLE','ALLOCATED'))
);

CREATE TABLE IF NOT EXISTS waiting_queue (
    queue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    equipment_id INTEGER NOT NULL,
    position INTEGER NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(equipment_id) REFERENCES equipment(equipment_id)
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    equipment_id INTEGER,
    action TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(equipment_id) REFERENCES equipment(equipment_id)
);
