class Drink:
    valid_bases = ['water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    valid_flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']

    def __init__(self, base):
        if base not in Drink.valid_bases:
            raise ValueError(f"Invalid base: {base}")
        self.__base = base
        self.__flavors = set()

    def get_base(self):
        return self.__base

    def get_flavors(self):
        return list(self.__flavors)

    def get_total(self):
        return 1

    def get_num_flavors(self):
        return len(self.__flavors)

    def set_flavors(self, flavors):
        for flavor in flavors:
            self.add_flavor(flavor)

    def add_flavor(self, flavor):
        if flavor in Drink.valid_flavors:
            self.__flavors.add(flavor)
        else:
            raise ValueError(f"Invalid flavor: {flavor}")


class Order:
    def __init__(self):
        self.__items = []

    def get_items(self):
        return self.__items

    def get_num_items(self):
        return len(self.__items)

    def get_total(self):
        return sum(item.get_total() for item in self.__items)

    def add_item(self, drink):
        if isinstance(drink, Drink):
            self.__items.append(drink)
        else:
            raise TypeError("Item must be of type Drink")

    def remove_item(self, index):
        if 0 <= index < len(self.__items):
            del self.__items[index]
        else:
            raise IndexError("Invalid index")
