from classes.inventory_item import InventoryItem
from db.db_conn import create_table
import sqlite3

class ItemRepository:
    def __init__(self):
        create_table() # creates inventory table if it doesn't exist

    def add_item(self, item: InventoryItem):
        # TODO: pass item to database
        # TODO: add id to new item
        query = """
                INSERT INTO inventory (name, price, quantity, description) VALUES (?, ?, ?, ?)
                """
        with sqlite3.connect("inventory.db") as conn: # commits and closes 
            c = conn.cursor()
            c.execute(query, (item.name, item.price, item.quantity, item.description)) 

            item.id = c.lastrowid


    def del_from_db(self, item: InventoryItem):
        pass

    def get_item(self, id: int):
        pass

    def get_all_items(self):
        query = """
                SELECT * FROM inventory;
                """
        with sqlite3.connect("inventory.db") as conn:
            c = conn.cursor()
            c.execute(query)

            inv_data = c.fetchall()

        return inv_data