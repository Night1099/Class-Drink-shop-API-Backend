import unittest
from menu_item import MenuItem

class TestMenuItem(unittest.TestCase):
    def setUp(self):
        # Initialize a MenuItem instance for each test case
        self.item = MenuItem("Test Item", 10.0)

    def test_add_topping(self):
        # Test adding a topping to the menu item
        self.item.add_topping("Test Topping")
        self.assertIn("Test Topping", self.item.toppings)

    def test_get_total(self):
        # Test getting the total price of the menu item
        self.assertEqual(self.item.get_total(), 10.0)

    def test_str_representation(self):
        # Test the string representation of the menu item
        self.item.add_topping("Test Topping")
        self.assertEqual(str(self.item), "Test Item with Test Topping")

if __name__ == '__main__':
    unittest.main()