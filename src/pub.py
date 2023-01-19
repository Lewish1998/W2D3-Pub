class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = {
            'Vodka': [3.50, 2],
            'Sambuca': [3.50, 3],
            'Red Wine': [4.99, 2],
            'Venom': [9.50, 8],
            'Goodbye Liver': [17.35, 25]
        }
        self.food = {
            'Chips': [2.75, 2],
            'Onion Rings': [3.50, 2],
            'Macaroni Cheese': [8.50, 4],
            "Fish 'n' Chips": [11.25, 5]
        }

    def of_age(self, customer):
        return customer.age >= 18


    def check_stock(self):
        for drink in self.drinks:
            