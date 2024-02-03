class Drink:
    valid_bases = ['water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    valid_flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']
    size_prices = {'small': 1.50, 'medium': 1.75, 'large': 2.05, 'mega': 2.15}
    flavor_price = 0.15

    def __init__(self, base, size):
        if base not in Drink.valid_bases:
            raise ValueError(f"Invalid base: {base}")
        if size.lower() not in Drink.size_prices:
            raise ValueError(f"Invalid size: {size}")
        self._base = base
        self._flavors = set()
        self._size = size.lower()
    
    def set_size(self, size):
        if size.lower() in Drink.size_prices:
            self._size = size.lower()
        else:
            raise ValueError(f"Invalid size: {size}")

    def get_size(self):
        return self._size

    def get_base(self):
        return self._base

    def get_flavors(self):
        return list(self._flavors)

    def get_num_flavors(self):
        return len(self._flavors)

    def set_flavors(self, flavors):
        if all(flavor in Drink.valid_flavors for flavor in flavors):
            self._flavors = set(flavors)
        else:
            invalid = [flavor for flavor in flavors if flavor not in Drink.valid_flavors]
            raise ValueError(f"Invalid flavors: {invalid}")

    def add_flavor(self, flavor):
        if flavor in Drink.valid_flavors:
            self._flavors.add(flavor)
        else:
            raise ValueError(f"Invalid flavor: {flavor}")

    def get_total(self):
        total = Drink.size_prices[self._size]
        total += len(self._flavors) * Drink.flavor_price
        return total
