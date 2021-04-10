#  Square Rectangle Inheritance
#
# Define the Square class, which we will use as a base class
class Square():
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def getSize(self):
        return self.size

    def getColor(self):
        return self.color

    def getArea(self):
        area = self.size * self.size
        return area


# Define a SquareWithBorder class that will be a subclass
# It will inherit from the Square class
class SquareWithBorder(Square):
    def __init__(self, size, color, borderColor, borderSize=1):
        self.borderColor = borderColor
        self.borderSize = borderSize
        super().__init__(size, color)

    def getBorderColor(self):
        return self.borderColor

    def getBorderSize(self):
        return self.borderSize

# Create objects
oSquare = Square(5, 'red')
oSquareWithBorder = SquareWithBorder(5, 'blue', 'green', 2)

# Call methods of the Square object
print(oSquare.getColor())
print(oSquare.getSize())
print(oSquare.getArea())

# Call methods of the SquareWithBorder object
print(oSquareWithBorder.getColor())
print(oSquareWithBorder.getSize())
print(oSquareWithBorder.getBorderColor())
