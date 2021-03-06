
import sortedlist


class SortedDict(dict):

    def __init__(self, dictionary=None, key=None, **kwargs):
        dictionary = dictionary or {}
        super().__init__(dictionary)
        if kwargs:
            super().update(kwargs)
        self.__keys = sortedlist.SortedList(super().keys(), key)


    def update(self, dictionary=None, **kwargs):
        if dictionary is None:
            pass
        elif isinstance(dictionary, dict):
            super().update(dictionary)
        else:
            for key, value in dictionary.items():
                super().__setitem__(key, value)
        if kwargs:
            super().update(kwargs)
        self.__keys = SortedList.SortedList(super().keys(),
                                            self.__keys.key)

    @classmethod
    def fromkeys(cls, iterable, value=None, key=None):
        return cls({k: value for k in iterable}, key)


    def value_at(self, index):
        return self[self.__keys[index]]


    def set_value_at(self, index, value):
        self[self.__keys[index]] = value


    def clear(self):
        super().clear()
        self.__keys.clear()


    def setdefault(self, key, value=None):
        if key not in self:
            self.__keys.add(key)
        return super().setdefault(key, value)


    def pop(self, key, *args):
        if key not in self:
            if len(args) == 0:
                raise KeyError(key)
            return args[0]
        self.__keys.remove(key)
        return super().pop(key, args)


    def popitem(self):
        item = super().popitem()
        self.__keys.remove(item[0])
        return item


    def values(self):
        for key in self.__keys:
            yield self[key]


    def items(self):
        for key in self.__keys:
            yield (key, self[key])


    def __iter__(self):
        return iter(self.__keys)

    keys = __iter__


    def __delitem__(self, key):
        try:
            self.__keys.remove(key)
        except ValueError:
            raise KeyError(key)
        return super().__delitem__(key)


    def __setitem__(self, key, value):
        if key not in self:
            self.__keys.add(key)
        return super().__setitem__(key, value)


    def __repr__(self):
        return object.__repr__(self)


    def __str__(self):
        return ("{" + ", ".join(["{0!r}: {1!r}".format(k, v)
                                 for k, v in self.items()]) + "}")


    def copy(self):
        d = SortedDict()
        super(SortedDict, d).update(self)
        d.__keys = self.__keys.copy()
        return d

    __copy__ = copy



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    d = SortedDict(dict(s=1, A=2, y=6), str.lower)
    d["z"] = 4
    d["T"] = 5
    del d["y"]
    d["n"] = 3
    d["A"] = 17
    print(str(d)) # returns: "{'A': 17, 'n': 3, 's': 1, 'T': 5, 'z': 4}"
