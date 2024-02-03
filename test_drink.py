import unittest
from Drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink('water', 'Small')

    def test_get_base(self):
        self.assertEqual(self.drink.get_base(), 'water')

    def test_get_flavors(self):
        self.drink.add_flavor('lemon')
        self.assertIn('lemon', self.drink.get_flavors())

    def test_get_num_flavors(self):
        self.assertEqual(self.drink.get_num_flavors(), 0)
        self.drink.add_flavor('lemon')
        self.assertEqual(self.drink.get_num_flavors(), 1)

    def test_get_size(self):
        self.assertEqual(self.drink.get_size(), 'Small')

    def test_set_flavors(self):
        self.drink.set_flavors(['lemon', 'mint'])
        self.assertEqual(set(['lemon', 'mint']), set(self.drink.get_flavors()))

    def test_set_size(self):
        self.drink.set_size('Large')
        self.assertEqual(self.drink.get_size(), 'large')

    def test_get_total_with_size_and_flavors(self):
        self.drink.set_size('Medium')
        self.drink.add_flavor('lemon')
        self.drink.add_flavor('mint')
        expected_total = Drink.size_prices['medium'] + 2 * Drink.flavor_price
        self.assertEqual(self.drink.get_total(), expected_total)

if __name__ == '__main__':
    unittest.main()
