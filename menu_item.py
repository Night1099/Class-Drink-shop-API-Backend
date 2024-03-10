class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.toppings = []

    def add_topping(self, topping):
        # Add a topping to the menu item
        self.toppings.append(topping)

    def get_total(self):
        # Calculate the total price of the menu item
        return self.price

    def __str__(self):
        # Return a string representation of the menu item
        toppings_str = ", ".join(self.toppings)
        return f"{self.name} with {toppings_str}"