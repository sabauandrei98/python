from domain.client import client
from exceptions.exceptions import raiseException
from validation.validator import clientValidator

class clientsControllerException(raiseException):
    pass

class clientsController:

    def __init__(self, clientRepository):
        self.__clientRepository = clientRepository
        self.__clientValidator = clientValidator()

    '''
    CLIENTS
    '''

    def add_client(self, arg):
        c = client(arg[0], arg[1])
        self.__clientValidator.validate(c)
        self.__clientRepository.addItem(c)

    def remove_client(self, id):
        self.__clientValidator.validateId(id)
        self.__clientRepository.removeItem(id)

    def update_client(self, arg):
        c = client(arg[0], arg[1])
        self.__clientValidator.validate(c)
        self.__clientRepository.updateItem(c)

    def get_clients(self):
        return self.__clientRepository.getItems()

    def getItem(self, id):
        return self.__clientRepository.getItemById(id)

    def search_client(self, arg):
        l = []
        books = self.__clientRepository.getItems()
        for x in books:
            if arg == x.getId() or arg == x.getName():
                l.append(x)
        return l


