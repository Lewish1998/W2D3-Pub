class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def buy_drink(self, drink, pub):
        if pub.of_age(self):
            self.wallet -= drink.price
            pub.till += drink.price
            # alcohol_level
        

    