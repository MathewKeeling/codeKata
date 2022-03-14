import lottery
import unittest
import random

#  test broke

class Test(unittest.TestCase):

    def test_sortedRack(self):
        rack = lottery.Rack()

        tumbler = lottery.Tumbler()
        tumbler.populate()

        self.assertEqual({}, rack.balls)

        rack.add(20)
        self.assertEqual({ 20:1 }, rack.balls)

        rack.add(40)
        self.assertEqual({ 20:1, 40:1 }, rack.balls)

    def test_drawing(self):
        rack = lottery.Rack()
        
        tumbler = lottery.Tumbler()
        tumbler.populate()

        randomInt = random.randint(5, 15)
        for i in range(0, randomInt):
            rack.add(tumbler.get_ball())

        rack.displayRack()
        print(rack.rackstate)

        self.assertEqual(randomInt, len(rack.balls))

if __name__ == '__main__':
    unittest.main()