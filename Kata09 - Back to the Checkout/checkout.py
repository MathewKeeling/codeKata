#  information about classes and objects in Python
#  https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html

class Product:
    def __init__(self, name, price, discQty, discAmt):
        self.name = name
        self.price = price
        self.discQty = discQty
        self.discAmt = discAmt

    def get_price(self, number_to_be_bought):
        cost, discount = 0, 0
        discount = number_to_be_bought // discQty * discAmt
        cost = ( price * number_to_be_bought ) + discount
        return cost

def checkout(cart):
    
    print("Your total is: ", total)

products = {
  "a": [50, 3, -20],
  "b": [30, 2, -15],
  "c": [20, 1, 0],
  "d": [15, 1, 0]
}

total = 0
itemQty = [0] * len(products)
cart = "aaa"

for letter in cart:
    index = ord(letter) - 96
    itemQty[index - 1] += 1

x = 0
while x < len(products):
    item = str(chr(x + 97))
    name = item
    price = products[item][0]
    discQty = products[item][1]
    discAmt = products[item][2]
    productSelected = Product(name, price, discQty, discAmt)
    total = total + productSelected.get_price(itemQty[x])
    x += 1

print("Your total is: ", total)

