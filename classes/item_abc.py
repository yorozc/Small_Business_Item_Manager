from abc import ABC, abstractmethod

class Item(ABC):

    def __init__(self, name: str, price: float, quantity: int, description: str):
        self.id = None
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    # TODO: create validation for attributes

    
    
