import unittest
from src.pub import Pub
from src.customer import Customer
from src.drinks import Drinks
from src.food import Food


class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink = Drinks('Vodka', 3.50, 2)
        self.pub = Pub('The Pedo and the Swan', 500)
        self.customer = Customer('Super Hanz', 80, 45)
        self.food = Food('Chips', 2.75, 2)

    def test_buy_drink(self):
        self.customer.buy_drink(drink=self.drink, pub=self.pub)
        customer_wallet = self.customer.wallet
        pub_till = self.pub.till
        self.assertEqual(76.50, customer_wallet)
        self.assertEqual(503.50, pub_till)

    def test_of_age(self):
        self.assertEqual(True, self.pub.of_age(self.customer))
    

    def test_buy_drink_age_check(self):
        self.customer.buy_drink(drink=self.drink, pub=self.pub)
        customer_wallet = self.customer.wallet
        pub_till = self.pub.till
        self.assertEqual(76.50, customer_wallet)
        self.assertEqual(503.50, pub_till)

    def test_has_alcohol(self):
        alcohol_level = self.drink.alcohol_level
        self.assertEqual(2, alcohol_level)

    def test_increase_drunkenness(self):
        self.customer.buy_drink(drink=self.drink, pub=self.pub)
        self.assertEqual(2, self.customer.drunkenness_level)

    def test_decline_too_drunk(self):
        drink = Drinks('Moonshine', 3.50, 20)
        self.assertEqual(False, self.customer.buy_drink(drink=drink, pub=self.pub))
        
    # def test_buy_food(self):
    #     self.customer.buy_food(self.pub, self.food)
        
