import sqlite3

def create_table():
    # creates db
    conn = sqlite3.connect('inventory.db')

    c = conn.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS inventory(
    name TEXT,
    price REAL,
    quantity INTEGER,
    description TEXT
    )
    """) # runs queries

    conn.commit()

    conn.close()