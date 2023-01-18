import unittest
from src.pub import Pub
from src.customer import Customer
from src.drinks import Drinks


class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drink = Drinks('Vodka', 3.50)
        self.pub = Pub('The Pedo and the Swan', 500)
        self.customer = Customer('Super Hanz', 80, 45)