from domain.rental import rental
from exceptions.exceptions import raiseException
from repository.repository import repository


class RentalCSVFileRepository(repository):
    def __init__(self, fileName="rental.txt"):
        repository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def addItem(self, item):
        repository.addItem(self, item)
        self.__storeToFile()

    def removeItem(self, id):
        repository.removeItem(self, id)
        self.__storeToFile()

    def updateItem(self, newItem):
        repository.updateItem(self, newItem)
        self.__storeToFile()

    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(",")
                item = rental(int(attrs[0]), int(attrs[1]), int(attrs[2]), attrs[3], attrs[4], attrs[5])
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
            strf = str(item.getId()) + "," + item.getBookId() + "," + item.getClientId() + "," + \
                   item.getRentedDate() + "," + item.getDueDate() + "," + item.getReturnedDate() + "\n"
            f.write(strf)
        f.close()
