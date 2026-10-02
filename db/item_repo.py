from classes.inventory_item import Inventory_Item
from db_conn import create_table
from queries import *

import sqlite3

class ItemRepository:
    def __init__(self):
        create_table(CREATE_TABLE) # creates inventory if it doesn't exist

    def add_item(self, item: Inventory_Item):
        pass

    def del_from_db(self, item: Inventory_Item):
        pass

    def get_item(self, id: int):
        pass

    def get_all_items(self):
        pass