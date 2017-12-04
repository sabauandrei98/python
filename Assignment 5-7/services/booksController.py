from domain.book import book
from exceptions.exceptions import raiseException
from validation.validator import bookValidator

class booksControllerException(raiseException):
    pass

class booksController:

    def __init__(self, bookRepository):
        self.__bookRepository = bookRepository
        self.__bookValidator = bookValidator()


    '''
    BOOKS
    '''
    def add_book(self, arg):
        print(arg)
        b = book(arg[0], arg[1], arg[2], arg[3])
        self.__bookValidator.validate(b)
        self.__bookRepository.addItem(b)

    def remove_book(self, id):
        self.__bookValidator.validateId(id)
        self.__bookRepository.removeItem(id)

    def update_book(self, arg):
        b = book(arg[0], arg[1], arg[2], arg[3])
        self.__bookValidator.validate(b)
        self.__bookRepository.updateItem(b)

    def get_books(self):
        return self.__bookRepository.getItems()

    def getItem(self, id):
        return self.__bookRepository.getItemById(id)

    def search_book(self, arg):
        l = []
        books = self.__bookRepository.getItems()
        for x in books:
            if arg == x.getId() or arg == x.getTitle() or arg == x.getDescription() or arg == x.getAuthor():
                l.append(x)
        return l




