from customer import customer_dictionary, Customer
from account import Checking_Account, Savings_Account

class Employee:
    def __init__(self, employee_ID, firstname, lastname, age, email):
        self.employee_ID = employee_ID
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email

    def view_customer_account_info(self, customer_ID):
        cust = customer_dictionary[customer_ID]
        return [cust.firstname,
                cust.lastname,
                cust.age,
                cust.email]

    def add_new_customer(self, customer_ID, firstname, lastname, age, email, balance, account_type, overdraft_limit):
        customer_dictionary[customer_ID] = Customer(firstname, lastname, age, email)
        customer_dictionary[customer_ID].make_account(balance, account_type, overdraft_limit)

class Manager(Employee):
    def switch_customer_account(self, customer_ID):
        print(customer_dictionary[customer_ID].__dict__)

    def change_customer_info(self, customer_ID, info_to_change, new_info):
        customer_dictionary[customer_ID].__dict__[info_to_change] = new_info

    def remove_customer(self, customer_ID):
        del customer_dictionary[customer_ID]

employee1 = Employee(123546, "Jackie", "Garrod", 48, "jackie.garrod@hotmail.com")
manager1 = Manager(123457, "Dave", "Garrod", 70, "dave.garrod@btinternet.com")
manager1.add_new_customer(100005, "Jamie", "Marten", 40, "jamie.marten@rocketmail.com", 10000, "current", 1000)
manager1.add_new_customer(100006, "james", "andrew", 41, "blah@gmail.com", 100000, "savings", 0)
#print(customer_dictionary)
manager1.change_customer_info(100005, 'firstname', "James")
#print(customer_dictionary[100005].firstname)
manager1.switch_customer_account(100005)
for i in Employee.view_customer_account_info(manager1, 100005):
    print(i)
