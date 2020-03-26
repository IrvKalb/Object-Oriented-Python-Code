# Main Employee Property Example

from Employee import *

oEmployee1 = Employee('Joe Schmoe', 99999)
oEmployee2 = Employee('Jane Smith', 123456)

print(oEmployee1.salary)
print(oEmployee2.salary)

oEmployee1.salary = 100000
oEmployee2.salary = 222222

print(oEmployee1.salary)
print(oEmployee2.salary)
