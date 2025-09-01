# lib/cash_register.py

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        amount = price * quantity
        self.total += amount
        for _ in range(quantity):
            self.items.append(title)
        self.last_transaction = amount

    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * (100 - self.discount) / 100)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        if self.total < 0:
            self.total = 0
        self.last_transaction = 0
