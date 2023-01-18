class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def of_age(self, customer):
        return customer.age >= 18



