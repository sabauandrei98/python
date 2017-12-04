from exceptions.exceptions import raiseException

class repositoryException(raiseException):
    pass

class repository:

    def __init__(self):
        self.__items = []

    def addItem(self, item):
        for x in self.__items:
            if int(item.getId()) == int(x.getId()):
                raise repositoryException("Duplicate id !!!")
        self.__items.append(item)


    def removeItem(self, id):
        found = False
        for x in self.__items:
            if int(x.getId()) == int(id):
                found = True
                self.__items.remove(x)

        if not found:
            raise repositoryException("Item not found !!!")

    def updateItem(self, item):
        found = False
        for x in self.__items:
            if int(x.getId()) == int(item.getId()):
                found = True
                self.__items[self.__items.index(x)] = item

        if not found:
            raise repositoryException("Item not found !!!")

    def getItems(self):
        return self.__items[:]

    def __len__(self):
        return len(self.__items)

    def getItemById(self, id):
        for x in self.__items:
            if int(x.getId()) == int(id):
                return x