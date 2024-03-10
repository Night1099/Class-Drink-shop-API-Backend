import unittest
from order import Order
from drink import Drink
from food import Food
from ice_storm import IceStorm

class TestOrder(unittest.TestCase):
    def setUp(self):
        # Initialize an Order instance and sample menu items for each test case
        self.order = Order()
        self.drink = Drink("Test Drink", "small")
        self.food = Food("Test Food", 5.0)
        self.ice_storm = IceStorm("Test Flavor")
        self.ice_storm.add_topping("Whipped Cream")
        self.ice_storm.add_topping("Chocolate Sauce")

    def test_add_item(self):
        # Test adding an item to the order
        self.order.add_item(self.drink)
        self.assertIn(self.drink, self.order.get_items())

    def test_remove_item(self):
        # Test removing an item from the order
        self.order.add_item(self.food)
        self.order.remove_item(0)
        self.assertNotIn(self.food, self.order.get_items())

    def test_get_num_items(self):
        # Test getting the number of items in the order
        self.order.add_item(self.drink)
        self.order.add_item(self.food)
        self.assertEqual(self.order.get_num_items(), 2)

    def test_get_total(self):
        # Test getting the total price of the order, including tax
        self.order.add_item(self.drink)
        self.order.add_item(self.food)
        self.order.add_item(self.ice_storm)
        expected_total = 1.50 + 5.0 + 0.50 + (1.50 + 5.0 + 0.50) * Order.tax_rate
        self.assertAlmostEqual(self.order.get_total(), expected_total, places=2)

    def test_generate_receipt(self):
        # Test generating a receipt for the order
        self.order.add_item(self.drink)
        self.order.add_item(self.food)
        self.order.add_item(self.ice_storm)
        receipt = self.order.generate_receipt()
        self.assertIn("Test Drink", receipt['items'][0])
        self.assertIn("Test Food", receipt['items'][1])
        self.assertIn("Test Flavor", receipt['items'][2])
        self.assertAlmostEqual(receipt['total_before_tax'], 7.0, places=2)
        self.assertAlmostEqual(receipt['tax'], 0.51, places=2)
        self.assertAlmostEqual(receipt['total'], 7.51, places=2)

if __name__ == '__main__':
    unittest.main()