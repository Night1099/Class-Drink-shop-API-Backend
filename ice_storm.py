from menu_item import MenuItem

class IceStorm(MenuItem):
    def __init__(self, flavor):
        # Initialize an IceStorm instance with a flavor
        super().__init__(flavor, 0)  # Price will be calculated based on toppings
        self.flavor = flavor

    def get_total(self):
        # Calculate the total price of the IceStorm based on toppings
        topping_prices = {
            'Cherry': 0.00,
            'Whipped Cream': 0.00,
            'Caramel Sauce': 0.50,
            'Chocolate Sauce': 0.50,
            'Storios': 1.00,
            'Dig Dogs': 1.00,
            "T&T's": 1.00,
            'Cookie Dough': 1.00,
            'Pecans': 0.50
        }
        total = 0
        for topping in self.toppings:
            total += topping_prices.get(topping, 0)
        return total