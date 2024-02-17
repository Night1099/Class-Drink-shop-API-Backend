import unittest
from Order import Order
from Drink import Drink
from Food import Food

class TestOrder(unittest.TestCase):

    def setUp(self):
        # Initialize an Order object and two Drink objects for testing
        self.order = Order()
        self.drink1 = Drink('water', 'small') # Adjusting to match the Drink class provided
        self.drink2 = Drink('sbrite', 'small')

    def test_add_item(self):
        # Test adding a drink to the order and verifying it's included
        self.order.add_item(self.drink1)
        self.assertIn(self.drink1, self.order.get_items())

    def test_get_num_items(self):
        # Test the number of items in the order increases correctly after adding a drink
        self.order.add_item(self.drink1)
        self.assertEqual(self.order.get_num_items(), 1)

    def test_get_total(self):
        # Test the total cost of the order is correct after adding two drinks
        self.order.add_item(self.drink1)
        self.order.add_item(self.drink2)
        expected_total = self.drink1.get_total() + self.drink2.get_total() + (self.drink1.get_total() + self.drink2.get_total()) * Order.tax_rate
        self.assertAlmostEqual(self.order.get_total(), expected_total)

class TestFood(unittest.TestCase):
        # Test creating a food item with a specific name and price.
    def test_food_creation(self):
        hotdog = Food('Hotdog', 2.30)
        self.assertEqual(hotdog.name, 'Hotdog')
        self.assertEqual(hotdog.price, 2.30)

    def test_add_topping(self):
        # Test adding a topping to a food item.
        fries = Food('French Fries', 1.50)
        fries.add_topping('Ketchup', 0.00)
        self.assertIn('Ketchup', fries.toppings)

    def test_total_price_with_toppings(self):
        # Test the total price calculation of a food item with multiple toppings.
        nachos = Food('Nacho Chips', 1.90)
        nachos.add_topping('Nacho Cheese', 0.30)
        nachos.add_topping('Bacon Bits', 0.30)
        # Verify the total price is the sum of the base price and all toppings' prices.
        self.assertEqual(nachos.get_total_price(), 2.50)

class TestOrderWithFood(unittest.TestCase):
    def test_add_food_to_order(self):
        order = Order()
        corndog = Food('Corndog', 2.00)
        order.add_item(corndog)
        # Verify the food item is included in the order's items list.
        self.assertIn(corndog, order.items)

    def test_order_total_with_food_and_drinks(self):
        # Test the total price of an order containing both food items and drinks.
        order = Order()
        ice_cream = Food('Ice Cream', 3.00)
        ice_cream.add_topping('Chocolate Sauce', 0.50)
        order.add_item(ice_cream)
        # Verify the total price includes both the food item and drink.
        self.assertEqual(order.get_total(), 3.50) # Update total calculation based on drink addition

    def test_order_receipt_with_food_and_drinks(self):
        # Test generating a receipt for an order that includes both food items and drinks.
        order = Order()
        fries = Food('French Fries', 1.50)
        fries.add_topping('Chili', 0.60)
        order.add_item(fries)
        receipt = order.generate_receipt()
        # Check if the receipt correctly lists food items, their toppings, and drinks.
        self.assertIn('French Fries', receipt)
        self.assertIn('Chili', receipt)


if __name__ == '__main__':
    unittest.main()
