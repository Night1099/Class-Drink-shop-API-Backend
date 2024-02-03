import unittest
from Order import Order
from Drink import Drink

class TestOrder(unittest.TestCase):

    def setUp(self):
        self.order = Order()
        self.drink1 = Drink('water', 'Small')
        self.drink2 = Drink('sbrite', 'Medium')

    def test_add_item(self):
        self.order.add_item(self.drink1)
        self.assertIn(self.drink1, self.order.get_items())

    def test_get_num_items(self):
        self.order.add_item(self.drink1)
        self.assertEqual(self.order.get_num_items(), 1)

    def test_get_total(self):
        self.order.add_item(self.drink1)
        self.order.add_item(self.drink2)
        self.assertEqual(self.order.get_total(), self.drink1.get_total() + self.drink2.get_total())

if __name__ == '__main__':
    unittest.main()
