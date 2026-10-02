import sqlite3

def create_table(query):
    # creates db
    conn = sqlite3.connect('inventory.db')

    c = conn.cursor()

    c.execute(query) # runs queries

    conn.commit()

    conn.close()