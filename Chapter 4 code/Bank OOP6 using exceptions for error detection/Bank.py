# Bank that manages a dictionary of account objects

from Account import *


class Bank():

    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0

    def openAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        # Increment to prepare for next account to be created
        self.nextAccountNumber = self.nextAccountNumber + 1
        return newAccountNumber

    def openAccountInteractively(self):
        print('*** Open Account ***')
        userName = input('What is your name? ')
        userStartingAmount = input('How much money to have to start you account with? ')
        userStartingAmount = float(userStartingAmount)
        userPassword = input('What password would you like to use for this account? ')

        userAccountNumber = self.openAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)
        print()

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = input('What is your account number? ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('What is your password? ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)

        print('You had', theBalance, 'in your account, which is being returned to you.')
        del self.accountsDict[userAccountNumber]
        print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        try:
            theBalance = oAccount.getBalance(userAccountPassword)
        except Exception as errorMessage:
            print(errorMessage)
            return
        if theBalance >= 0:
            print('Your balance is:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        accountNum = input('Please enter the account number: ')
        accountNum = int(accountNum)
        depositAmount = input('Please enter amount to deposit: ')
        depositAmount = float(depositAmount)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[accountNum]
        try:
            theBalance = oAccount.deposit(depositAmount, userAccountPassword)
        except Exception as errorMessage:
            print(errorMessage)
            return
        print('Your new balance is:', theBalance)

    def show(self):
        print('*** Show ***')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('Account', userAccountNumber)
            oAccount.show()

    def withdraw(self):
        print('*** Withdraw ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAmount = input('Please enter the amount to withdraw: ')
        userAmount = float(userAmount)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        try:
            theBalance = oAccount.withdraw(userAmount, userAccountPassword)
        except Exception as errorMessage:
            print(errorMessage)
            return

        print('Withdrew:', userAmount)
        print('Your new balance is:', theBalance)
