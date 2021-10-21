
class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def give_raise(self, percent):
        self.salary = self.salary + (self.salary + percent)
    def work(self):
        print(self.name, "does stuff")
    def __repr__(self):
        return f"<Employee: name={self.name}, salary={self.salary}>"

class Chef(Employee):
    def __init__(self, name):
        super().__init__(name,  salary=50000)
    def work(self):
        print(self.name, "makes food")

class Server(Employee):
    def __init__(self, name):
        super().__init__(name, salary=40000)
    def work(self):
        print(self.name, "interfaces with customers")

class PizzaRobot(Chef):
    def __init__(self, name):
        super().__init__(name)
    def work(self):
        print(self.name, "makes pizza")
