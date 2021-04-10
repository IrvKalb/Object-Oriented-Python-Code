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

    def __init__(self, window, shapeType, maxWidth, maxHeight):
        if type(shapeType) is Shape:
            raise TypeError('You cannot instantiate a Shape object directly.')
        self.window = window
        self.shapeType = shapeType
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)

    def getType(self):
        return self.shapeType

    def clickedInside(self, mousePoint):
        raise NotImplementedError('Subclass must implement the method: clickedInside')

    def getArea(self):
        raise NotImplementedError('Subclass must implement the method: area')

    def draw(self):
        raise NotImplementedError('Subclass must implement the method: draw')

