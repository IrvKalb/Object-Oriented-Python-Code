# Non-OOP
# Bank 2
# Single account

accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

   
def show():
    global accountName, accountBalance, accountPassword
    print('       Name', accountName)
    print('       Balance:', accountBalance)
    print('       Password:', accountPassword)
    print()

def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect password')
        return -1
    return accountBalance

def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return -1
        
    if password != accountPassword:
        print('Incorrect password')
        return -1
    
    accountBalance = accountBalance + amountToDeposit
    return accountBalance
    
def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return -1

    if amountToWithdraw > accountBalance:
        print('You cannot withdraw more than you have in your account')
        return -1

    if password != accountPassword:
        print('Incorrect password for this account')
        return -1
    
    accountBalance = accountBalance - amountToWithdraw
    return accountBalance


newAccount("Joe", 100.00, 'soup')  # create an account

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower() # force lower case
    action = action[0]  # just use first letter
    print()
    
    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userPassword)
        if theBalance >= 0:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = float(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance >= 0:
            print('Your new balance is:', newBalance)       

    elif action == 's':   #show
        print('Show:')
        show()

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')

        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = float(userWithdrawAmount)
        userPassword = input('Please enter the password: ')
 
        newBalance = withdraw(userWithdrawAmount, userPassword)
        if newBalance >= 0:
            print('Your new balance is:', newBalance)      

print('Done')
