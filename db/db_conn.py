import sqlite3

def create_table():
    # creates db
    conn = sqlite3.connect('inventory.db')

    c = conn.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS inventory(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    description TEXT
    );
    """) # runs queries

    conn.commit()

    conn.close()