# Person example main program using direct access

from Person import *

oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('Jane Smith', 99000)

# Get the values of the salary variable directly
print(oPerson1.salary)
print(oPerson2.salary)

# Change the salary variable directly
oPerson1.salary = 100000
oPerson2.salary = 111111

# Get the updated salaries and print again
print(oPerson1.salary)
print(oPerson2.salary)

