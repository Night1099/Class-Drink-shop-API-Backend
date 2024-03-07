"""
A blueprint for creating drink objects
"""

class Drink:
    # Define valid bases and flavors for drinks, ensuring that only acceptable inputs are used for drink creation.
    valid_bases = ['water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    valid_flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']
    
    # Pricing structure based on drink size and additional cost for flavor.
    size_prices = {'small': 1.50, 'medium': 1.75, 'large': 2.05, 'mega': 2.15}
    flavor_price = 0.15 # Additional cost for each flavor added to the drink.

    def __init__(self, base, size='small'):  # Default size set to 'small' if not provided
        # Initialize a Drink instance, enforcing validation on base and size to ensure they are valid options.
        self.base = base.lower()
        self.size = size.lower()
        if self.base not in Drink.valid_bases:
            raise ValueError(f"Invalid base: {base}") # Ensures base is within the predefined list of valid bases.
        if self.size not in Drink.size_prices:
            raise ValueError(f"Invalid size: {size}") # Validates size against the predefined size pricing structure.
        self.flavors = []

    def add_flavor(self, flavor):
        # Add a flavor to the drink, validating against the list of valid flavors.
        if flavor.lower() not in Drink.valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}")
        self.flavors.append(flavor.lower())

    def get_size(self):
        # Return the size of the drink
        return self.size

    def set_size(self, size):
        # Set the size of the drink, ensuring it's a valid option
        if size.lower() not in Drink.size_prices:
            raise ValueError(f"Invalid size: {size}")
        self.size = size.lower()

    def get_total(self):
        # Calculate the total cost of the drink based on its size and number of flavors added.
        total = Drink.size_prices[self.size] + len(self.flavors) * Drink.flavor_price
        return total

    def get_base(self):
        # Return the base of the drink as a string
        return self.base

    def get_flavors(self):
        # Return a list of flavors added to the drink
        return self.flavors

    def get_num_flavors(self):
        # Return the count of flavors added to the drink
        return len(self.flavors)

    def set_flavors(self, flavors):
        # Set the flavors for the drink, replacing any existing flavors
        # Validates each flavor against the list of valid flavors
        for flavor in flavors:
            if flavor.lower() not in Drink.valid_flavors:
                raise ValueError(f"Invalid flavor: {flavor}")
        self.flavors = [flavor.lower() for flavor in flavors]

    def __str__(self):
        # Return a string representation of the Drink object
        flavor_str = ", ".join(self.flavors) if self.flavors else "no flavors"
        return f"{self.size} {self.base} with {flavor_str}"