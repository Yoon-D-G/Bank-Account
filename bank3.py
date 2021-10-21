

customer_dict = {}

class Checking_Account:
    def __init__(self, balance):
        self.balance = balance

    def withdrawal(self, amount, overdraft_limit=0):
        self.withdrawal -= amount
        return 'Thank you for your withdrawal. Your current balance is now {}'.format(self.balance)

    def interest(self):
        self.balance *= 1.02

class Savings_Account(Checking_Account):
    withdrawals = 0
    def withdrawal(self, amount):
        if withdrawals = 7:
            return 'Cannot make more than 7 withdrawals'
        self.balance -= amount
        withdrawal += 1

    def interest(self):
        self.balance *= 1.07

class Customer:
    def __init__(self, identity_number, firstname, lastname, age, email):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        customer_dict[identity_number] = self

    def withdrawal(self):
        pass


class Employee(Customer):
    def create_customer(self, identity_number, firstname, lastname, age, email):
        customer_dict[identity_number] = Customer(identity_number, firstname, lastname, age, email)

    def customer_details(self, identity_number):
        customer_list = []


class Manager(Employee):
    def __init__(self):
        pass

employee1 = Employee()
