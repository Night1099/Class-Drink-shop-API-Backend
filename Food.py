class Food:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.toppings = {}

    def add_topping(self, topping, cost):
        # Add a topping to the food item with its associated cost
        self.toppings[topping] = cost

    def get_total_price(self):
        # Calculate the total price of the food item including base price and toppings
        total_price = self.base_price
        for topping, cost in self.toppings.items():
            total_price += cost
        return total_price

    def get_name(self):
        # Return the name of the food item
        return self.name

    def get_toppings(self):
        # Return a dictionary of toppings and their costs for the food item
        return self.toppings

    def get_flavors(self):
        # Return an empty list to maintain compatibility with the Drink class
        return []

    def get_base(self):
        # Return the name of the food item as the base
        return self.name

    def get_num_flavors(self):
        # Return 0 as food items don't have flavors
        return 0

    def __str__(self):
        # Return a string representation of the Food object
        toppings_str = ", ".join(self.toppings.keys())
        return f"{self.name} with {toppings_str}"