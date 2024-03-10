from menu_item import MenuItem

class Food(MenuItem):
    def __init__(self, name, price):
        # Initialize a Food instance with a name and price
        super().__init__(name, price)