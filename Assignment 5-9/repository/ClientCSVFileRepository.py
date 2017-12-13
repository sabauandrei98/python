from domain.client import client
from exceptions.exceptions import raiseException
from repository.repository import repository


class ClientCSVFileRepository(repository):
    def __init__(self, fileName="client.txt"):
        repository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def addItem(self, item):
        repository.addItem(self, item)
        self.__storeToFile()

    def removeItem(self, id):
        repository.removeItem(self, id)
        self.__storeToFile()

    def update(self, newItem):
        repository.updateItem(self, newItem)
        self.__storeToFile()

    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                item = client(int(attrs[0]), attrs[1])
                repository.addItem(self, item)
                line = f.readline().strip()
        except IOError:
            raise raiseException("Error saving file")
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "w")
        repo = repository.getItems(self)
        for item in repo:
            strf = str(item.getId()) + "," + item.getName() + "\n"
            f.write(strf)
        f.close()
