# Vector class and test code:

class Vector():
    '''The Vector class represents two values as a vector, allows for many math calculations'''   
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'This vector has an x of ' + str(self.x) + ' and a y of ' + str(self.y)

    def __add__(self, oOther):  # called for + operator
        return Vector(self.x + oOther.x, self.y + oOther.y)

    def __sub__(self, oOther):  # called for - operator
        return Vector(self.x - oOther.x, self.y - oOther.y)

    def __mul__(self, oOther):  # called for * operator
        return (self.x * oOther.x) + (self.y * oOther.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __eq__(self, oOther):  # called for == operator
        return (self.x == oOther.x) and (self.y == oOther.y)

    def __ne__(self, oOther):  # called for != operator
        return not self.__eq__(oOther)  # reuse __eq__

    def __lt__(self, oOther):    # called for < operator
        if self.__abs__() < oOther.__abs__():
            return True
        else:
            return False
        
    def __gt__(self, oOther):  # called for > operator
        if self.__abs__() > oOther.__abs__():
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


