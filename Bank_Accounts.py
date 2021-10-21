
class Current_Account:

    def __init__(self, balance=0, overdraft_limit=0):
        if 'Current' in str(self.__class__):
            self.account_type = True
            self.overdraft_limit = int(input("Type overdraft limit: "))
        else:
            self.account_type = False
            self.overdraft_limit = overdraft_limit
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdrawal(self, withdrawal_amount):
        if (self.balance - withdrawal_amount) < -self.overdraft_limit:
            return "Cannot go below overdraft limit."
        else:
            self.balance -= withdrawal_amount

    def interest(self):
        if not self.account_type:
            self.balance *= 1.07
        else:
            self.balance *= 1.02

class Savings_Account(Current_Account):

    def __init__(self):
        super().__init__()
        self.number_of_withdrawals = 0

    def withdrawal(self, withdrawal_amount):
        if self.number_of_withdrawals == 7:
            return "You have reached maximum allowable withdrawals for Savings Account."
        if self.balance - withdrawal_amount < 0:
            return "Balance cannot be less than 0."
        self.balance -= withdrawal_amount
        self.number_of_withdrawals += 1
