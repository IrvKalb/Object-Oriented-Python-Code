# Person Example main program using direct access

from Person import *

oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('Jane Smith', 99000)

# Get the values of the salaries directly
print(oPerson1.salary)
print(oPerson2.salary)

# Change the salaries directly
oPerson1.salary = 100000
oPerson2.salary = 111111

# Get the salaries and print again
print(oPerson1.salary)
print(oPerson2.salary)

