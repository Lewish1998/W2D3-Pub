class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.food = []

    def of_age(self, customer):
        return customer.age >= 18



