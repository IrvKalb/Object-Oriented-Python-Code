# Test code for basic push and pop on a stack

from Stack import *

oStack = Stack()
oStack.push(5)
oStack.push(12)
oStack.push('Some data')
oStack.push('Some more data')
oStack.push(True)
oStack.show()

while True:
    print()
    item = oStack.pop()
    print('Next value from the stack is:', item)
    if oStack.getSize() == 0:
        break
    oStack.show()

print('Stack is empty')
