import unittest
from Order import Order
from Drink import Drink

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

if __name__ == '__main__':
    unittest.main()
