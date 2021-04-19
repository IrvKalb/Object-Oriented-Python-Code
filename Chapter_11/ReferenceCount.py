#  Reference count example

class Square():
    def __init__(self, width, color):
        self.width = width
        self.color = color

# Instantiate an object
oSquare1 = Square(5, 'red')
print(oSquare1)
# Reference count of the Square object is 1

# Now set another variable to the same object
oSquare2 = oSquare1
print(oSquare2)
# Reference count of the Square object is 2
