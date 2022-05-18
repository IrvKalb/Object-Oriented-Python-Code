# Vector test code

from Vector import *

v1 = Vector(3, 4)
v2 = Vector(2, 2)
v3 = Vector(3, 4)

# These lines print Boolean or numeric values
print(v1 == v2) # False
print(v1 == v3) # True
print(abs(v1))  # 5
print(abs(v2))  # 2.8284...
print(v1 < v2)  # False
print(v1 > v2)  # True
print() # Spacing

# These lines print the vectors (calls the __str__() method)
print('Vector 1:', v1) # 3, 4
print('Vector 2:', v2) # 2, 2
print('Vector 1 + Vector 2:', v1 + v2)  # 5, 6
print('Vector 1 - Vector 2:', v1 - v2)  # 1, 2
print('Vector 1 times Vector 2:', v1 * v2)  # 6, 8
print('Vector 1 times 5:', v1 * 5)  # 15, 20
