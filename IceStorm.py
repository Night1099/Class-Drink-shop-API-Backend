class IceStorm:
    valid_flavors = {
        'Mint Chocolate Chip': 4.00,
        'Chocolate': 3.00,
        'Vanilla Bean': 3.00,
        'Banana': 3.50,
        'Butter Pecan': 3.50,
        "S'more": 4.00
    }
    
    valid_toppings = {
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
    
    def __init__(self, flavor):
        # Initialize an IceStorm instance with a flavor, validating against the list of valid flavors
        if flavor not in IceStorm.valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}")
        self.flavor = flavor
        self.toppings = []
    
    def add_topping(self, topping):
        # Add a topping to the IceStorm, validating against the list of valid toppings
        if topping not in IceStorm.valid_toppings:
            raise ValueError(f"Invalid topping: {topping}")
        self.toppings.append(topping)
    
    def get_flavors(self):
        # Return a list containing the flavor of the IceStorm
        return [self.flavor]
    
    def get_base(self):
        # Return the flavor of the IceStorm as the base
        return self.flavor
    
    def get_total(self):
        # Calculate the total cost of the IceStorm based on the flavor and toppings
        total = IceStorm.valid_flavors[self.flavor]
        for topping in self.toppings:
            total += IceStorm.valid_toppings[topping]
        return total
    
    def get_num_flavors(self):
        # Return 1 as IceStorm has only one flavor
        return 1
    
    def __str__(self):
        # Return a string representation of the IceStorm object
        toppings_str = ", ".join(self.toppings)
        return f"{self.flavor} Ice Storm with {toppings_str}"