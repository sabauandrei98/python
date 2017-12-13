from exceptions.exceptions import raiseException

class repositoryException(raiseException):
    pass


class dataStructure:
    def __init__(self):
        self.__elems = []
        self.__index = 0

    def __len__(self):
        return len(self.__elems)

    def __setitem__(self, key, value):
        for i in range(len(self.__elems)):
            if self.__elems[i].id == key:
                self.__elems[i] = value
                return
        self.__elems.append(value)

    def __getitem__(self, key):
        for i in range(len(self.__elems)):
            if self.__elems[i].id == key:
                return self.__elems[i]

        return None

    def __delitem__(self, key):
        poz = -1
        for i in range(len(self.__elems)):
            if self.__elems[i].id == key:
                poz = i
                break
        if poz != -1:
            del self.__elems[poz]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__elems):
            raise StopIteration
        elem = self.__elems[self.__index]
        self.__index += 1
        return elem


class item:
    def __init__(self, id, data):
        self.id = id
        self.data = data

    def __str__(self):
        return str(self.id) + " " + self.data