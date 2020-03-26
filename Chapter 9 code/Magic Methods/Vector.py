# Vector class and test code:

class Vector():
    '''The Vector class represents two values as a vector, allows for many math calculations'''   
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'This vector has an x of ' + str(self.x) + ' and a y of ' + str(self.y)

    def __add__(self, other):  # called for + operator
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # called for - operator
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # called for * operator
        return (self.x * other.x) + (self.y * other.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __eq__(self, other):  # called for == operator
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):  # called for != operator
        return not self.__eq__(other)  # reuse __eq__

    def __lt__(self, other):    # called for < operator
        if self.__abs__() < other.__abs__():
            return True
        else:
            return False
        
    def __gt__(self, other):  # called for > operator
        if self.__abs__() > other.__abs__():
            return True
        else:
            return False

v1 = Vector(3, 4)
v2 = Vector(2, 2)
v3 = Vector(3, 4)

print(v1 == v2) # False
print(v1 == v3)  # True
print(v1 + v2)  #  5, 6
print(v1 - v2)  # 1, 2
print(abs(v1))  # 5
print(abs(v2))  #2.8284...

print(v1 < v2)  # False
print(v1 > v2)  # True

print(v1)


