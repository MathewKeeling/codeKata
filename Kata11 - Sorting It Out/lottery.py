import random

class Rack:
    def __init__(self):
        self.balls = {}
        self.rackstate = []

    def add(self, int):
        self.balls[int] = 1

    def displayRack(self):
        #  No need to sort them. Just append incrementally
        #  Probably the same way to tackle the second problem. Just count the letters and then print the multiples
        #    incrementally.
        for x in range(61):
            if x in self.balls:
                self.rackstate.append(x + 1)
            else:
                pass
        
class Tumbler:
    def __init__(self):
        self.balls = {}

    def populate(self):
        for x in range(61):
            self.balls[x] = 1

    def get_ball(self):
        x = 1
        while x != 0:
            selection = random.randint(0, 59)
            if selection in self.balls:
                x = 0
            else:
                x = 1
        self.balls.pop(selection, None)
        return selection

#  test
rack = Rack()
tumbler = Tumbler()
tumbler.populate()
for x in range(5):
    rack.add(tumbler.get_ball())
rack.displayRack()
print(rack.rackstate)



