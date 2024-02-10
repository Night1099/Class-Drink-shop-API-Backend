import unittest
from Drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        # Initialize a Drink object with 'water' base and 'small' size for each test
        self.drink = Drink('water', 'small')

    def test_add_flavor(self):
        # Test adding a flavor to the drink
        self.drink.add_flavor('lemon')
        self.assertIn('lemon', self.drink.flavors, "Flavor should be added to the drink")

    def test_case_insensitive_base(self):
        # Test case insensitivity of the drink base
        drink = Drink('WATER', 'small')
        self.assertEqual(drink.base, 'water', "Base should be case insensitive")

    def test_case_insensitive_size(self):
        # Test case insensitivity of the drink size
        drink = Drink('water', 'SMALL')
        self.assertEqual(drink.size, 'small', "Size should be case insensitive")

    def test_get_size(self):
        # Test getting the size of the drink
        self.assertEqual(self.drink.get_size(), 'small', "Should return the correct size")

    def test_set_size(self):
        # Test setting the size of the drink
        self.drink.set_size('large')
        self.assertEqual(self.drink.size, 'large', "Should correctly set the drink size")

    def test_get_total(self):
        # Test calculating the total cost of the drink
        self.drink.add_flavor('lemon')
        self.drink.add_flavor('lime')
        expected_total = Drink.size_prices['small'] + 2 * Drink.flavor_price
        self.assertAlmostEqual(self.drink.get_total(), expected_total, "Should calculate the correct total cost")

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
        self.assertCountEqual(self.drink.get_flavors(), ['lemon', 'mint'])

if __name__ == '__main__':
    unittest.main()
