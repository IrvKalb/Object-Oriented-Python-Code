# Main Student property example

from Student import *

oStudent1 = Student('Joe Schmoe')
oStudent2 = Student('Jane Smith')

# Get the students' grades using the 'grade' property and print
print(oStudent1.grade)
print(oStudent2.grade)
print()

# Set new values using the 'grade' property
oStudent1.grade = 85
oStudent2.grade = 92

oStudent1.grade = 'abc'


print(oStudent1.grade)
print(oStudent2.grade)
