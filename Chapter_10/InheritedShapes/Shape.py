# Shape class
#
# To be used as a base class for other classes

import random
from abc import ABC, abstractmethod

# Set up the colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Shape(ABC):  # identifies this as an abstract base class

    def __init__(self, window, shapeType, maxWidth, maxHeight):
        self.window = window
        self.shapeType = shapeType
        self.color = random.choice((RED, GREEN, BLUE))
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)

    def getType(self):
        return self.shapeType

    @abstractmethod
    def clickedInside(self, mousePoint):
        raise NotImplementedError

    @abstractmethod
    def getArea(self):
        raise NotImplementedError

    @abstractmethod
    def draw(self):
        raise NotImplementedError

