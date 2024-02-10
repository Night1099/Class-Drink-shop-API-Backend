"""
The Order module includes functionality necessary for managing a customer's order.
It leverages the Drink class for item management, allowing for a interactive ordering system.
This system is capable of adding, removing, and calculating the total cost of an order.
"""

from Drink import Drink

class Order:
    # The Order class acts as a container for multiple Drink instances, representing a single customer's order.

    def __init__(self):
       #  Initializes the Order with an empty list.
        self._items = []

    def get_items(self):
        # Provides access to the current list of items in the order.
        return self._items

    def get_num_items(self):
        # Retrieve the counts of items currently in the order, summarizes without need of details of items.
        return len(self._items)

    def get_total(self):
        # Computes the total cost of the order by iterating over each item in the order and summing their individual totals.
        return sum(item.get_total() for item in self._items)

    def add_item(self, drink):
        # Adds a Drink item to the order. This method ensures that only items of type Drink can be added
        if isinstance(drink, Drink):
            self._items.append(drink)
        else:
            raise TypeError("Item must be of type Drink")

    def remove_item(self, index):
        # Removes an item from the order based on its position.
        if index < 0 or index >= len(self._items):
            raise IndexError("Item index is out of range")
        del self._items[index]
