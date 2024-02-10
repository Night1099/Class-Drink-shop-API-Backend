import unittest
from Drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        # Initialize a Drink object with 'water' base for each test
        self.drink = Drink('water')  # Adjusted to match Drink class initialization

    def test_get_base(self):
        # Test if the get_base method returns the correct base
        self.assertEqual(self.drink.get_base(), 'water')

    def test_get_flavors(self):
        # Test adding a flavor and checking it's in the drink's flavors
        self.drink.add_flavor('lemon')
        self.assertIn('lemon', self.drink.get_flavors())

    def test_get_num_flavors(self):
        # Test the count of flavors before and after adding a flavor
        self.assertEqual(self.drink.get_num_flavors(), 0)
        self.drink.add_flavor('lemon')
        self.assertEqual(self.drink.get_num_flavors(), 1)

    def test_set_flavors(self):
        # Test setting multiple flavors at once
        self.drink.set_flavors(['lemon', 'mint'])
        self.assertEqual(set(['lemon', 'mint']), set(self.drink.get_flavors()))

if __name__ == '__main__':
    unittest.main()
