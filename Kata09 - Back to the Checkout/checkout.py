#  information about classes and objects in Python
#  https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html


class Product:
    def __init__(self, name, price, discQty, discAmt):
        self.name = name
        self.price = price

    def get_price(self, name, number_to_be_bought):
        cost, discount = 0, 0
        cost = number_to_be_bought * price
        discount = number_to_be_bought // discQty * discAmt
        cost = cost + discount
        return cost

def checkout(goods):
    total = 0
    #  split characters
    #  sum the total of the various elements
    #  for each element
    #    instantiate object of Product class and get_price the quantity
    #  total = sum total of prices
    return total

products = {
  "a": [50, 3, -20],
  "b": [15, 2, -15],
  "c": [15, 1, 0],
  "d": [15, 1, 0]
}

# name = input('name:')
# amount = int(input('digit amount of items'))
# price = int(input('digit price of items'))

productSelected = "c"

name = productSelected
price = products[productSelected][0]
discQty = products[productSelected][1]
discAmt = products[productSelected][2]

a = Product(name, price, discQty, discAmt)

# quantity = int(input('digit amount of items to buy'))
q1 = 16
print(f'cost for {q1} * {a.name} = {a.get_price(a.name, q1)}')