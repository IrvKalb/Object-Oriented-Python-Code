#  Square Rectangle Inheritance
#
# Define the Square class, which we will use as a base class
class Square():
    def __init__(self, width, color):
        self.width = width
        self.color = color

    def getWidth(self):
        return self.width

    def getColor(self):
        return self.color

    def getArea(self):
        area = self.width * self.width
        return area


# Define a rectangle class that will be a subclass
# It will inherit from the Square class
class Rectangle(Square):
    def __init__(self, width, height, color):
        self.height = height
        super().__init__(width, color)

    def getHeight(self):
        return self.height

    def getArea(self):
        area = self.width * self.height
        return area

# Create objects
oSquare = Square(5, 'red')
oRectangle = Rectangle(5, 10, 'blue')

# Call methods of the Square object
print(oSquare.getColor())
print(oSquare.getWidth())
print(oSquare.getArea())

# Call methods of the Rectangle object
print(oRectangle.getColor())
print(oRectangle.getWidth())
print(oRectangle.getHeight())
print(oRectangle.getArea())
