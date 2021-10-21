
class attrdisplay:

    def gather_attrs(self):
        attrs = []
        for attr in self.__dict__:
            attrs.append('{}={}'.format(attr, getattr(self, attr)))
        return ','.join(attrs)

    def __str__(self):
        return '{0}: {1}'.format(self.__class__.__name__, self.gather_attrs())

    def recursive_print(self):
        return self.__class__.__dict__

if __name__ == "__main__":
    class Toptest(attrdisplay):
        count = 0
        def __init__(self):
            self.attr1 = Toptest.count
            self.attr2 = Toptest.count + 1
            Toptest.count += 2

        def gather_attrs(self):
            return 'spam'

    class Bottomtest(Toptest):
        pass

    x = Toptest()
    print(x)
