#  information about classes and objects in Python
#  https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html

class Product:
    def __init__(self, name, price, discQty, discAmt):
        self.name = name
        self.price = price
        self.discQty = discQty
        self.discAmt = discAmt

    def get_price(self, name, number_to_be_bought):
        cost, discount = 0, 0
        cost = number_to_be_bought * price
        discount = number_to_be_bought // discQty * discAmt
        cost = cost + discount
        return cost

def getPrice(good, q1):
    #  print(f'cost for {q1} * {good.name} = {good.get_price(good.name, q1)}')
    cost = good.get_price(good.name, q1)
    return cost

products = {
  "a": [50, 3, -20],
  "b": [30, 2, -15],
  "c": [20, 1, 0],
  "d": [15, 1, 0]
}

purchased = "DABABA".lower()
total = 0
qty = [0] * len(products)

for letter in purchased:
    index = ord(letter) - 96
    qty[index - 1] += 1

x = 0
while x < len(products):
    productSelected = str(chr(x + 97))
    name = productSelected
    price = products[productSelected][0]
    discQty = products[productSelected][1]
    discAmt = products[productSelected][2]
    productSelected = Product(name, price, discQty, discAmt)
    total = total + getPrice(productSelected, qty[x])
    x += 1

print(total)