from db.item_repo import ItemRepository
from classes.inventory_item import InventoryItem
import rich 

item_repo = ItemRepository()
spacer = "-" * 10
def run_tui():
    while True:
        print("Welcome to Item MGR")
        print("Select an operation: ")
        print("1. Add new item")
        print(spacer)
        print("2. Display all items")
        # TODO: other operations
        # TODO: use rich to make tui look nice
        user_inp = input("What operation would you like to perform: ")

        match user_inp:
            case "1": # add to db

                while True:
                    name = input("Name of item: ")
                    price = input("Price of item: ")
                    quantity = input("Quantity: ")
                    description = input("Description (optional): ")
                    confirmation = input(f"Is the information entered correctly (y/n) : {name}, {price}, {quantity}, {description} ")

                    if confirmation.lower() == "y" or confirmation.lower() == "yes":

                        new_item = InventoryItem(name, price, quantity, description)
                        item_repo.add_item(new_item)

                        inv_data = item_repo.get_all_items()
                        for item in inv_data:
                            print(item)

                        break

            case "2": # get all from db
                inv_data = item_repo.get_all_items()
                for item in inv_data:
                    print(spacer)
                    print(f"ID: {item[0]}")
                    print(f"Name: {item[1]}")
                    print(f"Price: ${item[2]:.2f}")
                    print(f"Quantity: {item[3]}")
                    print(f"Description: {item[4]}")
                    print(spacer)

        