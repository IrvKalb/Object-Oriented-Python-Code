# Person Example main program

from Person import *

oPerson1 = Person('Joe Schmoe')
oPerson2 = Person('Jane Smith')

# Using getter and setter
print(oPerson1.getName())
print(oPerson2.getName())

oPerson1.setName('Fred Flintstone')
print(oPerson1.getName())

print()

print('Direct access')
print(oPerson1.name)
print(oPerson2.name)
oPerson1.name = 'John Smith'
print(oPerson1.name)
