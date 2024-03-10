import unittest
from ice_storm import IceStorm

class TestIceStorm(unittest.TestCase):
    def setUp(self):
        # Initialize an IceStorm instance for each test case
        self.ice_storm = IceStorm("Test Flavor")

    def test_get_total(self):
        # Test getting the total price of the IceStorm based on toppings
        self.ice_storm.add_topping("Whipped Cream")
        self.ice_storm.add_topping("Chocolate Sauce")
        self.assertEqual(self.ice_storm.get_total(), 0.50)

if __name__ == '__main__':
    unittest.main()