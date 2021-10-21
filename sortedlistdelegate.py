


import Util


_identity = lambda x: x


@Util.delegate("__list", ("pop", "__delitem__", "__getitem__",
                    "__iter__", "__reversed__", "__len__", "__str__"))
class SortedList:

    def __init__(self, sequence=None, key=None):
        self.__key = key or _identity
        assert hasattr(self.__key, "__call__")
        if sequence is None:
            self.__list = []
        elif (isinstance(sequence, SortedList) and
              sequence.key == self.__key):
            self.__list = sequence.__list[:]
        else:
            self.__list = sorted(list(sequence), key=self.__key)


    @property
    def key(self):
        return self.__key


    def clear(self):
        self.__list = []


    def __bisect_left(self, value):
        key = self.__key(value)
        left, right = 0, len(self.__list)
        while left < right:
            middle = (left + right) // 2
            if self.__key(self.__list[middle]) < key:
                left = middle + 1
            else:
                right = middle
        return key, left


    def add(self, value):
        index = self.__bisect_left(value)[1]
        if index == len(self.__list):
            self.__list.append(value)
        else:
            self.__list.insert(index, value)


    def remove(self, value):
        key, index = self.__bisect_left(value)
        while (index < len(self.__list) and
                self.__key(self.__list[index]) == key):
            if self.__list[index] == value:
                del self.__list[index]
                return
            index += 1
        raise ValueError("{0}.remove(x): x not in list".format(
                            self.__class__.__name__))


    def remove_every(self, value):
        count = 0
        key, index = self.__bisect_left(value)
        while (index < len(self.__list) and
               self.__key(self.__list[index]) == key):
            del self.__list[index]
            count += 1
        return count


    def count(self, value):
        count = 0
        key, index = self.__bisect_left(value)
        while (index < len(self.__list) and
               self.__key(self.__list[index]) == key):
            index += 1
            count += 1
        return count


    def index(self, value):
        key, index = self.__bisect_left(value)
        if (index < len(self.__list) and
            self.__key(self.__list[index]) == key):
            return index
        raise ValueError("{0}.index(x): x not in list".format(
                         self.__class__.__name__))


    def __setitem__(self, index, value):
        raise TypeError("use add() to insert a value and rely on "
                        "the list to put it in the right place")


    def __contains__(self, value):
        key, index = self.__bisect_left(value)
        return (index < len(self.__list) and
                self.__key(self.__list[index]) == key)


    def copy(self):
        return SortedList(self, self.__key)

    __copy__ = copy

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    letters = SortedList(("H", "c", "B", "G", "e"), str.lower)
    # str(letters) == "['B', 'c', 'e', 'G', 'H']"
    letters.add("G")
    letters.add("f")
    letters.add("A")
    # str(letters) == "['A', 'B', 'c', 'e', 'f', 'G', 'G', 'H']"
    letters[2] # returns: 'c'
