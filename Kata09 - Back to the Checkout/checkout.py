#  information about classes and objects in Python
#  https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html

class Product:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def print_name(self):
        print("This object's name is {}".format(self.name))
        return None

    def print_color(self):
        print("This object's color is {}".format(self.color))
        return None

class Price:
    def __init__(self, object):
        if object.name == "a":
            self.price = 50
        elif object.name == "b":
            self.price = 30
        elif object.name == "c":
            self.price = 20
        elif object.name == "d":
            self.price = 15
        else:
            return None

class Discount:
    def __init__(self, object):
        if object.name == "a":
            self.discount = [3, -20]
        elif object.name == "b":
            self.discount = [2, -15]
        elif object.name == "c":
            self.discount = [1, 0]
        elif object.name == "d":
            self.discount = [1, 0]
        else:
            print("The product has no associated discount.")
            return None

def checkout(cart):
    cart = cart.lower()
    itemQty = [0] * len(products)
    totalCost = 0

    #  counting the items to be purchased
    for letter in cart:
        index = ord(letter) - 96
        itemQty[index - 1] += 1

    #  getting the total for sum of each item: (itemPrice * itemQuantity) - itemDiscount
    counter = 0
    while counter < len(products):
        price = prices[counter].price
        discQty = discounts[counter].discount[0]
        discAmt = discounts[counter].discount[1]
        discount = ( itemQty[counter] // discQty ) * discAmt
        cost = ( price * itemQty[counter] ) + discount
        totalCost = totalCost + cost
        counter +=1
    return totalCost

products = [
    Product("a", "red"),
    Product("b", "orange"),
    Product("c", "yellow"),
    Product("d", "green")
    ]

prices = []
for product in products:
    prices.append(Price(product))

discounts = []
for product in products:
    discounts.append(Discount(product))


cart = "DABABA"

print("Total cost is: ")
print(checkout(cart))
