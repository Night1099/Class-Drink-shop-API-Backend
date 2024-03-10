from menu_item import MenuItem

class Drink(MenuItem):
    valid_sizes = ['small', 'medium', 'large', 'mega']
    size_prices = {'small': 1.50, 'medium': 1.75, 'large': 2.05, 'mega': 2.15}

    def __init__(self, name, size='small'):
        # Initialize a Drink instance with a name and size
        super().__init__(name, Drink.size_prices[size])
        self.size = size

    def get_size(self):
        # Return the size of the drink
        return self.size