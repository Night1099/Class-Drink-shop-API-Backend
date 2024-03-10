from drink import Drink
from food import Food
from ice_storm import IceStorm
from menu_item import MenuItem

class Order:
    tax_rate = 0.0725  # Tax rate of 7.25%

    def __init__(self):
        #  Initialize the Order with an empty list of items
        self._items = []

    def add_item(self, item):
        # Add a MenuItem instance to the order
        if not isinstance(item, MenuItem):
            raise ValueError("Only MenuItem instances can be added")
        self._items.append(item)

    def remove_item(self, index):
        # Remove an item from the order based on its index
        if index < 0 or index >= len(self._items):
            raise IndexError("Item index out of range")
        del self._items[index]

    def get_items(self):
        # Return the list of items in the order
        return self._items

    def get_num_items(self):
        # Return the number of items in the order
        return len(self._items)

    def get_total_before_tax(self):
        # Calculate the total cost of the order before tax
        return sum(item.get_total() for item in self._items)

    def get_total_tax(self):
        # Calculate the total tax for the order
        return self.get_total_before_tax() * Order.tax_rate

    def get_total(self):
        # Calculate the total cost of the order including tax
        return self.get_total_before_tax() + self.get_total_tax()

    def generate_receipt(self):
        # Generate a receipt for the order
        receipt = {
            'items': [str(item) for item in self._items],
            'total_before_tax': self.get_total_before_tax(),
            'tax': self.get_total_tax(),
            'total': self.get_total()
        }
        return receipt