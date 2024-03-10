import unittest
from drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        # Initialize a Drink instance for each test case
        self.drink = Drink("Test Drink", "small")

    def test_get_size(self):
        # Test getting the size of the drink
        self.assertEqual(self.drink.get_size(), "small")

    def test_get_total(self):
        # Test getting the total price of the drink
        self.assertEqual(self.drink.get_total(), 1.50)

if __name__ == '__main__':
    unittest.main()