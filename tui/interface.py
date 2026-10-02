from db.item_repo import ItemRepository
from classes.inventory_item import InventoryItem
import rich 

item_repo = ItemRepository()

def run_tui():
    while True:
        print("Welcome to Item MGR")
        print("Select an operation: ")
        print("1. Add new item")
        # TODO: other operations
        # TODO: use rich to make tui look nice
        user_inp = input("What operation would you like to perform: ")

        match user_inp:
            case "1": # add op
                while True:
                    name = input("Name of item: ")
                    price = input("Price of item: ")
                    quantity = input("Quantity: ")
                    description = input("Description (optional): ")
                    confirmation = input(f"Is the information entered correctly (y/n) : {name}, {price}, {quantity}, {description} ")

                    if confirmation.lower() == "y" or confirmation.lower() == "yes":
                        break
                new_item = InventoryItem(name, price, quantity, description)
                print(new_item)

                # item_repo.add_item(new_item)

            case "2":
                pass