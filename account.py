
class Checking_Account:
    def __init__(self, balance, overdraft_limit=0):
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def account_withdrawal(self, withdrawal_amount):
        if self.balance - withdrawal_amount < -self.overdraft_limit:
            print("Insufficient funds available")
        else:
            self.balance -= withdrawal_amount

    def interest(self):
        self.balance *= 1.02

class Savings_Account(Checking_Account):
    def interest(self):
        self.balance *= 1.07
