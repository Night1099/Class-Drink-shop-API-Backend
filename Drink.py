"""
    The Drink module defines the Drink class, which serves as a blueprint for creating drink objects
"""



class Drink:
    # Define valid bases and flavors for drinks, ensuring that only acceptable inputs are used for drink creation.
    valid_bases = ['water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    valid_flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']
    
    # Pricing structure based on drink size and additional cost for flavor.
    size_prices = {'small': 1.50, 'medium': 1.75, 'large': 2.05, 'mega': 2.15}
    flavor_price = 0.15  # Additional cost for each flavor added to the drink.

    def __init__(self, base, size):
        # Initialize a Drink instance, enforcing validation on base and size to ensure they are valid options.
        if base not in Drink.valid_bases:
            raise ValueError(f"Invalid base: {base}")  # Ensures base is within the predefined list of valid bases.
        if size.lower() not in Drink.size_prices:
            raise ValueError(f"Invalid size: {size}")  # Validates size against the predefined size pricing structure.
        self.base = base
        self.size = size
        self.flavors = []

    def add_flavor(self, flavor):
        # Add a flavor to the drink, validating against the list of valid flavors.
        if flavor in Drink.valid_flavors:
            self.flavors.append(flavor)
        else:
            raise ValueError(f"Invalid flavor: {flavor}")  # Restricts flavors to those predefined as valid.

    def get_total(self):
        # Calculate the total cost of the drink based on its size and number of flavors added.
        base_price = Drink.size_prices[self.size]  # Start with the base price determined by the size of the drink.
        # Add additional cost for each flavor added.
        total_flavor_price = len(self.flavors) * Drink.flavor_price
        return base_price + total_flavor_price