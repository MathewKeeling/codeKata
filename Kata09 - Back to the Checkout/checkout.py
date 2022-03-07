#  information about classes and objects in Python
#  https://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html

class Product:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def print_name(self):
        print("This object's name is {}".format(self.name))
        return None

    def print_price(self):
        print("This object's color is {}".format(self.color))
        return None

class Price:
    def __init__(self):
        self = self

class Discount:
    def __init__(self):
        self = self




#  "name": [weight, color]
products = [ 
    Product("a", "red"), 
    Product("b", "orange"), 
    Product("c", "yellow"), 
    Product("d", "green") 
    ]

Product.print_price(products[0])
