from account import Checking_Account, Savings_Account

customer_dictionary = {}

class Customer:
    def __init__(self, firstname, lastname, age, email):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.make_account_counter = 0


    def make_account(self, balance, account_type, overdraft_limit):
        if self.make_account_counter == 1:
            return "Can only open one account"
        else:
            if account_type == 'checking':
                self.account = Checking_Account(balance, overdraft_limit)
                self.make_account_counter += 1
            elif account_type == "savings":
                self.account = Savings_Account(balance)
                self.make_account_counter += 1


    def account_withdrawal(self, withdrawal_amount):
        self.account.account_withdrawal(withdrawal_amount)


customer1 = customer_dictionary[100001] = Customer("Ewen", "Garrod", 40, "ewen.garrod@gmail.com")
customer2 = customer_dictionary[100002] = Customer("Nyevero", "Simbanegavi", 38, "nyevero.simbanegavi@gmail.com")
customer3 = customer_dictionary[100003] = Customer("Ainslie", "Hancock", 37, "ainslie.hancock@hotmail.com")
customer4 = customer_dictionary[100004] = Customer("Jamal", "Abushena", 40, "jabushena@hotmail.com")
customer1.make_account(1000, "checking", 1500)
customer1.account_withdrawal(100)
print(customer1.account.balance)
customer1.account.interest()
print(customer1.account.balance)
