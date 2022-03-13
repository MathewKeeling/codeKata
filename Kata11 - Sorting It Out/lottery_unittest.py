import sorting
import unittest
import random

class Test(unittest.TestCase):

    def test_sortedRack(self):
        rack = sorting.Rack()

        tumbler = sorting.Tumbler()
        tumbler.populate()

        self.assertEqual([], rack.balls)

        rack.add(20)
        self.assertEqual([ 20 ], rack.balls)

        rack.add(40)
        self.assertEqual([ 20, 40 ], rack.balls)

    def test_drawing(self):
        tumbler = sorting.Tumbler()
        tumbler.populate()

        rack = sorting.Rack()

        randomInt = random.randint(5, 15)
        for i in range(0, randomInt):
            rack.add(tumbler.get_ball())

        self.assertEqual(randomInt, len(rack.balls))

if __name__ == '__main__':
    unittest.main()