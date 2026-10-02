import sqlite3

conn = sqlite3.connect('inventory.db')

c = conn.cursor() # runs db queries

c.execute()