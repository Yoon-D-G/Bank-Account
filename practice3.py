

class Adder:
    def add(self, x, y):
        print('Not implemented')

class ListAdder(Adder):
    def add(self, x, y):
        return x + y

class DictAdder(Adder):
    def add(self, a, b):
        a.update(b)
        return a

adder = Adder()
adder.add(1, 2)
x = [1, 2, 3]
y = ['a', 'b', 'c']
listadder = ListAdder()
print(listadder.add(x, y))
a = {'a': 1, 'b': 2, 'c': 3}
b = {'Ewen': 'Big', 'Davidson': 'Man', 'Garrod': 'Ting'}
dictadder = DictAdder()
print(dictadder.add(a, b))
