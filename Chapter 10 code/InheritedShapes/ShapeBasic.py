# Shape class
#
# Shape class - basic
#
import random

# set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Shape():  # This is an abstract class

    def __init__(self, window, whichShape):
        self.window = window
        self.type = whichShape
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(0, 400)
        self.y = random.randrange(0, 400)

    def getType(self):
        return self.type
