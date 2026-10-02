from classes.item_abc import Item

class InventoryItem(Item):
    def __init__(self, id, name, price, quantity, description):
        super().__init__(id, name, price, quantity, description)
