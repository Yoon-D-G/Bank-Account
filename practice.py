import practice3

class Super:
    def __init__(self, data):
        self.data = data
    def spam(self):
        self.attr1 = 1
        self.attr2 = 2

class Sub(Super, practice3.ListTree):
    def __init__(self, number, data):
        Super.__init__(self, data)
        self.number = number
    def ham(self):
        self.attr3 = 3

sub = Sub(1, 2)
print(sub)
