# Person Example main program using getters and setters

from Person import *

oPerson1 = Person('Joe Schmoe')
oPerson2 = Person('Jane Smith')

# Get the names using getter 
print(oPerson1.getName())
print(oPerson2.getName())

# Change the names using setter
oPerson1.setName('Ima Newname')
oPerson2.setName('Me Tu')

#Get the names and print again
print(oPerson1.getName())
print(oPerson2.getName())
