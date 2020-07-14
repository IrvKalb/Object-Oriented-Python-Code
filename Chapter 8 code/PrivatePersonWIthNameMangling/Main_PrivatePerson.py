# PrivatePerson Example main program

from PrivatePerson import *

oPrivatePerson1 = PrivatePerson('Joe Schmoe', 'Data for Joe Schmoe')
oPrivatePerson2 = PrivatePerson('Jane Smith', 'Data for Jane Smith')

# Using getter and setter - works fine
print(oPrivatePerson1.getName())

oPrivatePerson1.setName('Joseph Schmoe')
print(oPrivatePerson1.getName())


# Attempted use of direct access would fail
#print(oPrivatePerson1.__privateData)


# Using mangled name - works
print(oPrivatePerson1._PrivatePerson__privateData)
oPrivatePerson1._PrivatePerson__privateData = 'Modified data for Joeseph Schmoe'
print(oPrivatePerson1._PrivatePerson__privateData)


