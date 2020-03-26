# Account class

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = float(balance)
        self.password = password
   
    def deposit(self, amountToDeposit, password):
        if amountToDeposit < 0:
            print('You cannot deposit a negative amount!')
            return -1

        if password != self.password:
            print('Sorry, incorrect password')
            return -1
            
        self.balance = self.balance + amountToDeposit
        return self.balance
        
    def withdraw(self, amountToWithdraw, password):
        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount')
            return -1

        if amountToWithdraw > self.balance:
            print('You cannot withdraw more than you have in your account')
            return -1

        if password != self.password:
            print('Incorrect password for this account')
            return -1
        
        self.balance = self.balance - amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return -1
        return self.balance

    # Added for debugging
    def show(self):
        print('       Name', self.name)
        print('       Balance:', self.balance)
        print('       Password:', self.password)
        print()





