import unittest
from src.pub import Pub
from src.customer import Customer
from src.drinks import Drinks

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink = Drinks('Vodka', 3.50)
        self.pub = Pub('The Pedo and the Swan', 500)
        self.customer = Customer('Super Hanz', 80, 45)

    def test_buy_drink(self):
        self.customer.buy_drink(drink=self.drink, pub=self.pub)
        customer_wallet = self.customer.wallet
        pub_till = self.pub.till
        self.assertEqual(76.50, customer_wallet)
        self.assertEqual(503.50, pub_till)

    def test_of_age(self):
        self.assertEqual(True, self.pub.of_age(self.customer))
    

    def buy_drink_age_check(self):
        self.customer.buy_drink(drink=self.drink, pub=self.pub)
        customer_wallet = self.customer.wallet
        pub_till = self.pub.till
        self.assertEqual(76.50, customer_wallet)
        self.assertEqual(503.50, pub_till)