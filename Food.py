class Food:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.toppings = {}

    def add_topping(self, topping, cost):
        self.toppings[topping] = cost

    def get_total_price(self):
        total_price = self.base_price
        for topping, cost in self.toppings.items():
            total_price += cost
        return total_price

    def get_name(self):
        return self.name

    def get_toppings(self):
        return self.toppings
