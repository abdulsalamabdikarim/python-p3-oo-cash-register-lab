#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.items_with_multiples = []
        self.price_list = []
# here
    def add_item(self, title, price, quantity = 1):
        self.title = title
        self.price = price * quantity
        self.quantity = quantity
        self.total += self.price
        self.items.append(self.title)
        for x in range(self.quantity):
            self.items_with_multiples.append(self.title)

    def apply_discount(self):
          if self.discount > 0:
              self.total -= int((self.total * (self.discount/100)))
              print(f"After the discount, the total comes to ${self.total}.")
              return self.total
          else:
              print("There is no discount to apply.")
    
    def test_items_list_without_multiples(self):
        return self.items
    
    def test_items_list_with_multiples(self):
        return self.items_with_multiples
    
    def void_last_transaction(self):
        pass

y = CashRegister(20)
y.add_item("pen", 100, 3)
y.add_item("book", 100, 3)
y.add_item("glass", 100, 1)

z = y.apply_discount()

s = y.test_items_list_with_multiples()
# print(y.items)
print(y.items)
print(y.items_with_multiples)

print("paul " *3)

# g = 6
# print(float(g))
r = []
q = 7

for i in range(q):
    r.append(4)
print(r)

