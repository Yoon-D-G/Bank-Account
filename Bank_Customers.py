
from Bank_Accounts import Current_Account, Savings_Account

customer_dictionary = {} # customer ID is the key: customer object is the value
#firstname, lastname, age, email attributes

class Customer:

    def __init__(self, firstname, lastname, age, email):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.ID = self.make_customer_ID() # six-digit customer ID starting at 100000 and incrementing by 1 for every new customer
        customer_dictionary[self.ID] = self
        self.counter = 0

    def make_customer_ID(self):
        if not customer_dictionary:
            return 100000
        else:
            new_customer_id = sorted(customer_dictionary.keys()).pop() + 1
            return new_customer_id

    def create_account(self, account_type, overdraft_limit=0):
        if self.counter >= 1:
            print("only one account can be created")
        elif self.counter < 1 and account_type == "current":
            self.account = Current_Account()
            self.counter += 1
        elif self.counter < 1 and account_type == "savings":
            self.account = Savings_Account()
            self.counter += 1

    def __str__(self):
        return ('{0:.<25}{5}\n'
                '{1:.<25}{6}\n'
                '{2:.<25}{7}\n'
                '{3:.<25}{8}\n'
                '{4:.<25}{9}\n').format(
                'Customer ID',
                'Firstname',
                'Lastname',
                'Age',
                'Email',
                self.ID,
                self.firstname,
                self.lastname,
                self.age,
                self.email,
                )

if __name__ == '__main__':
    customer1 = Customer("Ewen", "Garrod", 40, "ewen.garrod@gmail.com")
    print(customer1)
    customer1.create_account("savings")
