import checkout    # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        products = [
            checkout.Product("a", "red"),
            checkout.Product("b", "orange"),
            checkout.Product("c", "yellow"),
            checkout.Product("d", "green")
            ]

        prices = []
        for product in products:
            prices.append(checkout.Price(product))

        discounts = []
        for product in products:
            discounts.append(checkout.Discount(product))


        self.assertEqual(checkout.checkout(""), 0)
        self.assertEqual(checkout.checkout("A"), 50)
        self.assertEqual(checkout.checkout("AB"), 80)
        self.assertEqual(checkout.checkout("CDBA"), 115)
        
        self.assertEqual(checkout.checkout("AA"), 100)
        self.assertEqual(checkout.checkout("AAA"), 130)
        self.assertEqual(checkout.checkout("AAAA"), 180)
        self.assertEqual(checkout.checkout("AAAAA"), 230)
        self.assertEqual(checkout.checkout("AAAAAA"), 260)

        self.assertEqual(checkout.checkout("AAAB"), 160)
        self.assertEqual(checkout.checkout("AAABB"), 175)
        self.assertEqual(checkout.checkout("AAABBD"), 190)
        self.assertEqual(checkout.checkout("DABABA"), 190)


if __name__ == '__main__':
    unittest.main()