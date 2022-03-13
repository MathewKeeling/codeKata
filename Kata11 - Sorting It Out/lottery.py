import random

class Rack:
    def __init__(self):
        self.balls = []
        
    def add(self, int):
        self.balls.append(int)
        self.balls.sort()
        

class Tumbler:
    def __init__(self):
        self.balls = {}
    
    def populate(self):
        for i in range(0, 60):
            self.balls[i] = 1
    
    def get_ball(self):
        i = 1
        while i != 0:
            selection = random.randint(0,59)
            if selection in self.balls:
                i = 0
            else:
                i = 1
        self.balls.pop(selection, None)
        return selection




