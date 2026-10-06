import sqlite3

DB_NAME = "lab_equipment.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_database():
    connection = get_connection()
    with open("../database/schema.sql", "r", encoding="utf-8") as schema:
        connection.executescript(schema.read())
    connection.commit()
    connection.close()
