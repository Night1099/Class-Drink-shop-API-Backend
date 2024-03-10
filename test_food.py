import unittest
from food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        # Initialize a Food instance for each test case
        self.food = Food("Test Food", 5.0)

    def test_get_total(self):
        # Test getting the total price of the food item
        self.assertEqual(self.food.get_total(), 5.0)

if __name__ == '__main__':
    unittest.main()