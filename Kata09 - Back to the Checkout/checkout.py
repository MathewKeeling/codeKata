class Product:
    def __init__(self, name, amount, price, discQty, discAmt):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, name, number_to_be_bought):
        cost, discount = 0, 0
        cost = number_to_be_bought * price
        discount = number_to_be_bought // discQty * discAmt
        cost = cost + discount
        return cost

    def make_Product(self, quantity):
        self.amount -= quantity

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
amount = 200
price = products[productSelected][0]
discQty = products[productSelected][1]
discAmt = products[productSelected][2]

a = Product(name, amount, price, discQty, discAmt)

# quantity = int(input('digit amount of items to buy'))
q1 = 4

print(f'cost for {q1} * {a.name} = {a.get_price(a.name, q1)}')
a.make_Product(q1)
print(f'remaining stock: {a.amount}\n')

print("Debug: Name: ", a.name)

print(16 % 18)