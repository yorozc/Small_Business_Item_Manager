from abc import ABC, abstractmethod

class Item(ABC):

    # TODO: add more attributes
    def __init__(self, name: str, price: float, quantity: int, description: str):
        self._id = None
        self._name = name
        self._price = price
        self._quantity = quantity
        self._description = description | None=None

    # name validation
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        if not name.strip():
            raise ValueError("Name cannot be empty.")

        self._name = name.strip()

    # price validation
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, int):
            price = float(price)

        if not isinstance(price, float):
            raise TypeError("Price must be a float.")

        if price < 0 :
            raise ValueError("Price cannot be negative.")

        self._price = price

    # quantity validation
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an int.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self._quantity = quantity


    # description validation
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):

        self._description = description
