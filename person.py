from classtools import attrdisplay

class Person(attrdisplay):
    def __init__(self, name, job, wage):
        self.name = name
        self.job = job
        self.wage = wage

    def get_lastname(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        one_plus_percent = 1 + percent
        self.wage *= one_plus_percent

    #def __repr__(self):
    #    return str('Person: {0}, {1}, £{2:,.2f}'.format(self.name, self.job, self.wage))

class Manager(Person):
    def __init__(self, name, job, wage):
        super().__init__(name, job, wage)

    def give_raise(self, percent, bonus):
        Person.give_raise(self, percent + bonus)

    #def __repr__(self):
    #    return 'self.__class__: {}, self.__class__.__name__: {}, self.__class__.__bases__: {}, self.__dict__: {}'.format(self.__class__,
    #    self.__class__.__name__, self.__class__.__bases__, self.__dict__)


person1 = Person("Ewen Garrod", "Progammer", 100000)
print(person1.get_lastname())
person1.give_raise(0.2)
print(person1.wage)
print(person1)
manager1 = Manager("Jamal Abushena", "manager", 45000)
manager1.give_raise(0.2, 0.1)
print(manager1)
