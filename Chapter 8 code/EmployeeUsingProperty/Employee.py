# Employee class example


class Employee():

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        print('Getting salary of', self.__name, 'which is:', self.__salary)
        return self.__salary      

    @salary.setter
    def salary(self, newSalary):
        print('Setting salary of', self.__name, 'to:', newSalary)
        self.__salary = newSalary

