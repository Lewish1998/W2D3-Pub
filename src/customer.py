class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness_level = 0

    def buy_drink(self, drink, pub):
        if pub.of_age(self):
            if self.drunkenness_level < 10:
                self.wallet -= drink.price
                pub.till += drink.price
                # alcohol_level
                self.drunkenness_level += drink.alcohol_level
            
        return False

    def buy_food(self, food, pub):
        self.wallet -= food.price
        pub.till += food.price
        self.drunkenness_level -= food.rejuvenation_level
    