# Access to instance variables using property

class Employee():

    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, newAddress):
        self.__address = newAddress


# Main Employee Property Example
oEmployee1 = Employee('Joe Schmoe', '123 This Street')
oEmployee2 = Employee('Jane Smith', '987 That Lane')

print(oEmployee1.address)
print(oEmployee2.address)
print()

# Now change the addresses of both employees, and print
oEmployee1.address = '555 Fifth Street'
oEmployee2.address = '555 Fifth Street'

print(oEmployee1.address)
print(oEmployee2.address)
