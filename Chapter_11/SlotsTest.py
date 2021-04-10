# Stanard example that uses a dictionary
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(x, y)

        # Try to create an additional instance variable
        self.color = 'black'  #works fine
        print(self.color)

oPoint = Point(3, 5)


class PointWithSlots():
    #Define slots for only two instance variables
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(x, y)

        # Try to create an additional instance variable
        # Should fail
        self.color = 'black'
        print(self.color)
        
oPointWithSlots = PointWithSlots(3, 5)
