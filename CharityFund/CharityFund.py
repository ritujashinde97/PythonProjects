
class CharityFund:
    def __init__(self,balance=1000000):
        self.balance = balance
    def save_fund(self,amount):
        self.balance += amount
        print('You saved fund of $ :' +str(amount))
    def spend_fund(self,amount):
        self.balance -= amount
        print('You spent fund of $ ' +str(amount))

    def invest(self,return_rate):
        self.balance *= 1 + return_rate
        print('You invested fund at return rate of ' +str(return_rate))

    def get_balance(self):
        if self.balance < 0:
            print("You got deficit of " +str(-self.balance))
            return self.balance
        else:
            print(self.balance)
    def is_danger(self):
        if self.balance < 50000:
            print("Danger. You have " + str(self.balance) + ' left')
            return self.balance < 50000

help_elderly = CharityFund()
print('Initial balance: ')
help_elderly.get_balance()
help_elderly.spend_fund(200000)
print('Current balance: ')
help_elderly.get_balance()
help_elderly.invest(-0.5)
print('Current balance: ')
help_elderly.get_balance()
help_elderly.save_fund(100000)
print('Current balance: ')
help_elderly.get_balance()
help_elderly.spend_fund(450001)
print('Current balance: ')
help_elderly.get_balance()
help_elderly.is_danger()







