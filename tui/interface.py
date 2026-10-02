from db.item_repo import ItemRepository

item_repo = ItemRepository()

def run_tui():
    while True:
        user_inp = input("What operation would you like to perform?")

        match user_inp:
            case "1":
                pass
            case "2":
                pass