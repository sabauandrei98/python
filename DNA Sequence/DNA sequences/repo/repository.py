from raiseEx import raiseException

class repositoryException(raiseException):
    pass

class repository():

    def __init__(self):
        self.__items = []

    def addItem(self, item):
        for x in self.__items:
            if x.getDna() == item.getDna():
                raise repositoryException("Duplicate dna !!!")
        self.__items.append(item)

    def filter(self, item):
        l = []
        for x in self.__items:
            if item.getDna() in x.getDna():
                l.append(x)
        self.__items = l

        return l

    def getItems(self):
        return self.__items[:]

    def __len__(self):
        return len(self.__items)


    def __str__(self):
        repo = ""
        for x in self.__items:
            repo += str(x) + '\n'

        return repo