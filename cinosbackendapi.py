class Drink:
    # Represents a drink with a base and optional flavors

    # Valid options for drink bases and flavors
    valid_bases = ['water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    valid_flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']

    def __init__(self, base):
        # Initializes a drink with a base and an empty set for flavors
        if base not in Drink.valid_bases:
            raise ValueError(f"Invalid base: {base}")
        self.__base = base
        self.__flavors = set()  # Prevents duplicate flavors

    def get_base(self):
        # Returns the drink's base
        return self.__base

    def get_flavors(self):
        # Returns the current flavors as a list
        return list(self.__flavors)

    def get_total(self):
        # Returns the total cost. Placeholder for more complex logic
        return 1

    def get_num_flavors(self):
        # Counts the number of unique flavors
        return len(self.__flavors)

    def set_flavors(self, flavors):
        # Sets multiple flavors at once
        for flavor in flavors:
            self.add_flavor(flavor)

    def add_flavor(self, flavor):
        # Adds a single flavor if it's valid
        if flavor in Drink.valid_flavors:
            self.__flavors.add(flavor)
        else:
            raise ValueError(f"Invalid flavor: {flavor}")


class Order:
    # Represents an order containing multiple drinks

    def __init__(self):
        # Starts with an empty list of drinks
        self.__items = []

    def get_items(self):
        # Returns all drinks in the order
        return self.__items

    def get_num_items(self):
        # Counts the drinks in the order
        return len(self.__items)

    def get_total(self):
        # Sums the cost of all drinks in the order
        return sum(item.get_total() for item in self.__items)

    def add_item(self, drink):
        # Adds a drink if it's of the Drink type
        if isinstance(drink, Drink):
            self.__items.append(drink)
        else:
            raise TypeError("Item must be of type Drink")

    def remove_item(self, index):
        # Removes a drink by its index, if valid
        if 0 <= index < len(self.__items):
            del self.__items[index]
        else:
            raise IndexError("Invalid index")
