# Main program for controlling a bank made up of accounts

# Bring in all the code of the Bank class
from Bank import *

# Create an instance of the Bank
oBank = Bank()

# Main code
# Create two test accounts
joesAccountNumber = oBank.openAccount('Joe', 100.00, 'JoesPassword')
print("Joe's account number is:", joesAccountNumber)

marysAccountNumber = oBank.openAccount('Mary', 12345.67, 'MarysPassword')
print("Mary's account number is:", marysAccountNumber)


while True:
    print()
    print('Press b to get an account balance')
    print('Press c to close an account')
    print('Press d to make a deposit')
    print('Press o to open a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]  # grab the first letter
    print()
    
    if action == 'b':
        oBank.balance()

    elif action == 'c':
        oBank.closeAccount()

    elif action == 'd':
        oBank.deposit()
        
    elif action == 'o':
        oBank.openAccountInteractively()

    elif action == 's':
        oBank.show()

    elif action == 'q':
        break

    elif action == 'w':
        oBank.withdraw()

    else:
        print('Sorry, that was not a valid action.  Please try again.')
        
print('Done')

