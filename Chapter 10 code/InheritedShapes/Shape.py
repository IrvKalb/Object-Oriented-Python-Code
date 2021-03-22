# Shape class
#
# To be used as a base class for other classes
#
import random

# set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Shape():  # This is an abstract class

    def __init__(self, window, whichShape, maxWidth, maxHeight):
        if type(self) is Shape:
            raise Exception('You cannot instantiate a Shape class directly.')
        self.window = window
        self.type = whichShape
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)

    def getType(self):
        return self.type

    def clickedInside(self, mousePoint):
        raise NotImplementedError('Subclass must implement the method: clickedInside')

    def area(self):
        raise NotImplementedError('Subclass must implement the method: area')

    def draw(self):
        raise NotImplementedError('Subclass must implement the method: draw')

