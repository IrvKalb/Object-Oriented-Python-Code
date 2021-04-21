#  Employee Manager Inheritance
#
# Define the Employee class, which we will use as a base class
class Employee():
    def __init__(self, name, title, ratePerHour=None):
        self.name = name
        self.title = title
        if ratePerHour is not None:
            ratePerHour = float(ratePerHour)
        self.ratePerHour = ratePerHour

    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def payPerYear(self):
        # 52 weeks times 5 days a week * 8 hours per day
        pay = 52 * 5 * 8 * self.ratePerHour
        return pay


# Define a Manager subclass that inherits from Employee
class Manager(Employee):
    def __init__(self, name, title, salary, reportsList):
        self.salary = float(salary)
        self.reportsList = reportsList
        super().__init__(name, title)

    def getReports(self):
        return self.reportsList

    def payPerYear(self, giveBonus):
        pay = self.salary
        if giveBonus:
            pay = pay + (.10 * self.salary)  # add a bonus of 10%
            print(self.name, 'gets a bonus for good work')
        return pay       


    # Additional methods unique to Manager
    def addEmployee(self, employeeToAdd):
        self.reports.append(employeeToAdd)

    def removeEmployee(self, employeeToRemove):
        self.reports.pop(employeeToRemove)


# Create objects
oEmployee1 = Employee('Joe Schmoe', 'Pizza Maker', 16)
oEmployee2 = Employee('Chris Smith', 'Cashier', 14)
oManager = Manager('Sue Jones', 'Pizza Restaurant Manager',
                             55000, [oEmployee1, oEmployee2])

# Call methods of the Employee objects
print('Employee name:', oEmployee1.getName())
print('Employee salary:', '{:,.2f}'.format(oEmployee1.payPerYear()))
print('Employee name:', oEmployee2.getName())
print('Employee salary:', '{:,.2f}'.format(oEmployee2.payPerYear()))
print()

# Call methods of the Manager object
managerName = oManager.getName()
print('Manager name:', managerName)
# Give the manager a bonus
print('Manager salary:', '{:,.2f}'.format(oManager.payPerYear(True)))
print(managerName, '(' + oManager.getTitle() + ')', 'direct reports:')
reportsList = oManager.getReports()
for oEmployee in reportsList:
    print('   ', oEmployee.getName(),
            '(' + oEmployee.getTitle() + ')')
