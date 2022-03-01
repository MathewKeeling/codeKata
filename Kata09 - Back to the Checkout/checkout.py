#  information about classes and objects in Python
#  https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html

class Product:
    def __init__(self, name, price, discQty, discAmt):
        self.name = name
        self.price = price
        self.discQty = discQty
        self.discAmt = discAmt

    def get_price(self, number_to_be_bought):
        discQty = self.discQty
        discAmt = self.discAmt
        price = self.price
        cost, discount = 0, 0
        discount = number_to_be_bought // discQty * discAmt
        cost = ( price * number_to_be_bought ) + discount
        return cost

def checkout(cart):
    products = {
        "a": [50, 3, -20],
        "b": [30, 2, -15],
        "c": [20, 1, 0],
        "d": [15, 1, 0]
    }
    
    itemQty = [0] * len(products)

    totalCost = 0
    for letter in cart:
        index = ord(letter) - 96
        itemQty[index - 1] += 1
    
    counter = 0
    while counter < len(products):
        item = str(chr(counter + 97))
        name = item
        price = products[item][0]
        discQty = products[item][1]
        discAmt = products[item][2]
        itemSelected = Product(name, price, discQty, discAmt)
        totalCost = totalCost + itemSelected.get_price(itemQty[counter])
        counter += 1
    
    return totalCost

cart = "aaaaaa"
print("Your total cost is: ", checkout(cart))

