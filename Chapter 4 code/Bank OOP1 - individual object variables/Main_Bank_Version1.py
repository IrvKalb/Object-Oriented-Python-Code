# Test program using accounts
# Version 1 using object variables for each account

# Ask Python to bring in all the code from the Account class file
from Account import *

# Create two accounts:
oJoesAccount = Account('Joe', 100.00, 'JoesPassword')
print("Created an account for Joe")

oMarysAccount = Account('Mary', 12345.67, 'MarysPassword')
print("Created an account for Mary")

oJoesAccount.show()
oMarysAccount.show()
print()

# Call some methods on the different accounts
print('Calling methods of the two accounts ...')
oJoesAccount.deposit(50.00, 'JoesPassword')
oMarysAccount.withdraw(345.67, 'MarysPassword')
oMarysAccount.deposit(100.00, 'MarysPassword')

# Show the accounts
oJoesAccount.show()
oMarysAccount.show()

# Create another account with information from the user
print()
userName = input('What is the name for a new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = float(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oNewAccount = Account(userName, userBalance, userPassword)

# Show the newly created user account
oNewAccount.show()

# Let's deposit 100 into the new account
oNewAccount.deposit(100.00, userPassword)
usersBalance = oNewAccount.getBalance(userPassword)
print()
print('After depositing 100, users balance is:', usersBalance)

# Show the new account
oNewAccount.show()

