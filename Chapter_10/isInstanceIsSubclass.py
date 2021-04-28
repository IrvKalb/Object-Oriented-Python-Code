#  Testing isinstance and issubclass
class Base():

    def __init__(self):
        print('In Base init method')

class Sub(Base):

    def __init__(self):
        print('In Subclass init method')

oSub = Sub() # create an instance of the Sub class
oBase = Base()  # create an instance of the Base class

print(isinstance(oSub, Sub))  # returns True
print(isinstance(oSub, Base))  # returns True

print(isinstance(oBase, Base))  # returns True
print(isinstance(oBase, Sub))  # returns False

print(issubclass(Sub, Base))  # returns True
print(issubclass(Base, Sub))  # returns False
