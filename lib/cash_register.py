#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append(title)
        self.last_transaction_amount = price * quantity
        self.total += self.last_transaction_amount

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            return f"After the discount, the total comes to ${int(self.total)}."
        else:
            return "There is no discount to apply."
    
    def reset_register_total(self):
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def void_last_transaction(self):
        if self.items:
            for _ in range(self.last_transaction_amount // (self.total / len(self.items))):
                self.items.pop()
            self.total -= self.last_transaction_amount
            self.last_transaction_amount = 0



