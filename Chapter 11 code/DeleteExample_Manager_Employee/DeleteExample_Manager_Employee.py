# Employee class
class Employee():
    def __init__(self, name):
        self.name = name
        print('Creating employee', self.name)

    def __del__(self):
        print('In the __del__ method for employee:', self.name)

#Manager class
class Manager():
    def __init__(self):
       print('Creating the manager object')
       self.oEmployee1 = Employee('Joe')
       self.oEmployee2 = Employee('Sue')
       self.oEmployee3 = Employee('Chris')

    def __del__(self):
        print('In the __del__ method for Manager')

# Instantiate the manager object (that creates employees)
oManager = Manager()

# Delete the manager object
del oManager
