# Account class
# Errors handled by "raise" statements

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = float(balance)
        self.password = password
   
    def deposit(self, amountToDeposit, password):
        if amountToDeposit < 0:
            raise Exception('You cannot deposit a negative amount!')   

        if password != self.password:
            raise Exception('Sorry, incorrect password')   
            
        self.balance = self.balance + amountToDeposit
        return self.balance
        
    def withdraw(self, amountToWithdraw, password):
        if amountToWithdraw < 0:
            raise Exception('You cannot withdraw a negative amount')

        if amountToWithdraw > self.balance:
            raise Exception('You cannot withdraw more than you have in your account')

        if password != self.password:
            raise Exception('Incorrect password for this account')
        
        self.balance = self.balance - amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            raise Exception('Sorry, incorrect password') 

        return self.balance

    # Added for debugging
    def show(self):
        print('       Name', self.name)
        print('       Balance:', self.balance)
        print('       Password:', self.password)
        print()

    def getInfo(self):
        return self.name, self.balance, self.password




##    def getInterestRate(self):
##        
##        if self.balance < 1000:
##            self.interestRate = .01
##        elif self.balance < 10000:
##            self.interestRate = .02
##        else:
##            self.interestRate = .03
##        return self.interestRate
##
##    def getInterestRate(self, interestRate):
##        self.interestRate = interestRate
