import pickle
from repository.repository import repository

class PickleFileRepository(repository):
    def __init__(self, fileName="repo.pickle"):
        repository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()

    def addItem(self, item):
        repository.addItem(self, item)
        self.__storeToFile()

    def removeItem(self, id):
        repository.removeItem(self, id)
        self.__storeToFile()

    def update(self, item):
        repository.updateItem(self, item)
        self.__storeToFile()

    def __loadFromFile(self):
        f = open(self.__fName, "rb")

        """
        You cannot unpickle an empty file
            - EOFError means the file is empty
            - Exception means no file, not accessible and so on...
            - finally makes sure we close the input file, regardless of error
        """
        try:
            self.__items = pickle.load(f)
        except EOFError:
            self.__items = {}
        except Exception as e:
            raise e
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "wb")
        print(self.__items)
        pickle.dump(self.__items, f)
        f.close()