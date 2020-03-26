# Bank that manages a dictionary of account objects
# Detects errors with try/except

from Account import *

class Bank():

    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0

    def openAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        self.nextAccountNumber = self.nextAccountNumber + 1
        self.accountsDict[self.nextAccountNumber] = oAccount
        return self.nextAccountNumber

    def openAccountInteractively(self):
        print('*** Open Account ***')
        userName = input('What is your name? ')
        userStartingAmount = input('How much cash to start? ')
        try:
            userStartingAmount = float(userStartingAmount)
        except:
            print('The starting amount must be a floating point number.')
            return
        userPassword = input('What password would you like to use for this account? ')
        try:
            userAccountNumber = self.openAccount(userName, userStartingAmount, userPassword)
        except Exception as errorMessage:
            print(errorMessage)
            return
        print('Your new account number is:', userAccountNumber)
        print()

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = input('What is your account number? ')
        try:
            userAccountNumber = int(userAccountNumber)
        except:
            print('The account number must be an integer')
            return
        userPassword = input('What is your password? ')
        oAccount = self.accountsDict[userAccountNumber]
        try:
            theBalance = oAccount.getBalance(userPassword)
        except Exception as errorMessage:
            print(errorMessage)
            return

        print('You had', theBalance, 'in your account, which is being returned to you.')
        del self.accountsDict[userAccountNumber]
        print('Your account is now closed.')
        

    def balance(self):
        print('*** Get Balance ***')
        userAccountNumber = input('Please enter your account number: ')
        try:
            userAccountNumber = int(userAccountNumber)
        except:
            print('The account number must be an integer')
            return
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        try:
            theBalance = oAccount.getBalance(userAccountPassword)
        except Exception as errorMessage:
            print(errorMessage)
            return

        print('Your balance is:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        accountNumber = input('Please enter the account number: ')
        try:
            accountNumber = int(accountNumber)
        except:
            print('The account number must be an integer.')
            return
        userDepositAmount = input('Please enter amount to deposit: ')
        try:
            userDepositAmount = float(userDepositAmount)
        except:
            print('The amount deposited must be a floating point number.')
            return
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[accountNumber]
        try:
            theBalance = oAccount.deposit(userDepositAmount, userAccountPassword)
        except Exception as errorMessage:
            print(errorMessage)
            return
        print('Your new balance is:', theBalance)

    def show(self):
        print('*** Show ***')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            accountName, accountBalance, accountPassword = oAccount.getInfo()
            print('Account', userAccountNumber)
            print('       Name', accountName)
            print('       Balance:', accountBalance)
            print('       Password:', accountPassword)
            print()
            

    def withdraw(self):
        print('*** Withdraw ***')
        userAccountNumber = input('Please enter your account number: ')
        try:
            userAccountNumber = int(userAccountNumber)
        except:
            print('The account number must be an integer')
            return

        userWithdrawalAmount = input('Please enter the amount to withdraw: ')
        try:
            userWithdrawalAmount = float(userWithdrawalAmount)
        except:
            print('The amount to withdraw must be a floating point number')
            return
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        try:
            theBalance = oAccount.withdraw(userWithdrawalAmount, userAccountPassword)
        except Exception as errorMessage:
            print(errorMessage)
            return

        print('Withdrew:', userWithdrawalAmount)
        print('Your new balance is:', theBalance)
