from classes.inventory_item import InventoryItem
from db.db_conn import create_table
import sqlite3

class ItemRepository:
    def __init__(self):
        create_table() # creates inventory if it doesn't exist

    def add_item(self, item: InventoryItem):
        pass

    def del_from_db(self, item: InventoryItem):
        pass

    def get_item(self, id: int):
        pass

    def get_all_items(self):
        pass