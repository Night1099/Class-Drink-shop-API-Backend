from Drink import Drink

class Order:
    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items

    def get_num_items(self):
        return len(self._items)

    def get_total(self):
        return sum(item.get_total() for item in self._items)

    def add_item(self, drink):
        if isinstance(drink, Drink):
            self._items.append(drink)
        else:
            raise TypeError("Item must be of type Drink")

    def remove_item(self, index):
        if 0 <= index < len(self._items):
            del self._items[index]
        else:
            raise IndexError("Invalid index")
