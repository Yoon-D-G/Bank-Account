from Bank_Customers import Customer, customer_dictionary

employee_dictionary = {}

class Employee:
    def __init__(self, firstname, lastname, age, email):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.employee_ID = self.make_employee_ID() # six-digit customer ID starting at 999999 and decrementing by 1 for every new employee
        employee_dictionary[self.employee_ID] = self

    def make_employee_ID(self):
        if not employee_dictionary:
            return 999999
        else:
            new_employee_id = sorted(employee_dictionary.keys()).pop() + 1
            return new_employee_id

    def create_customer(self):
        firstname = input("Firstname: ")
        lastname = input("Lastname: ")
        age = int(input("Age: "))
        email = input("Email Address: ")
        account_type = input("Current or Savings Account: ")
        Customer(firstname, lastname, age, email, account_type)

    def view_customer(self):
        print(customer_dictionary[lastname])


if __name__ == '__main__':
    employee1 = Employee("Dave", "Garrod", 70, "dave.garrod@gmail.com")
    for key, value in employee_dictionary.items():
        for k, v in value.__dict__.items():
            print(k, v)
    employee1.view_customer()
