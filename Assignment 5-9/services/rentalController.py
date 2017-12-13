from domain.rental import rental
from exceptions.exceptions import raiseException
from validation.validator import bookValidator, clientValidator, rentalValidator
from collections import Counter
from utils import tools
import time
import operator

class rentalControllerException(raiseException):
    pass

class rentalController:

    def __init__(self, bookRepository, clientRepository, rentalRepository):
        self.__bookRepository = bookRepository
        self.__clientRepository = clientRepository
        self.__rentalRepository = rentalRepository

        self.__bookValidator = bookValidator()
        self.__clientValidator = clientValidator()
        self.__rentalValidator = rentalValidator()



    def getItem(self, id):
        return self.__rentalRepository.getItemById(id)

    def cancel_rental(self, id):
        rentals = self.__rentalRepository.getItems()
        for item in rentals:
            if int(item.getBookId()) == id:
                item.setReturnedDate("-")
                self.__rentalRepository.updateItem(item)

    '''
    RENT
    '''

    def rent_book(self, arg):
        r = rental(arg[0], arg[1], arg[2], time.strftime("%d/%m/%Y"), arg[3], "-")
        self.__rentalValidator.validate(r)

        rentals = self.__rentalRepository.getItems()
        books = self.__bookRepository.getItems()
        clients = self.__clientRepository.getItems()

        for x in rentals:
            if int(x.getId()) == int(r.getId()):
                raise rentalControllerException("Duplicate id !!!")
            if int(x.getBookId()) == int(r.getBookId()) and x.getReturnedDate() == '-':
                raise rentalControllerException("This book is already rented !!!")

        found = False
        for x in books:
            if int(x.getId()) == int(r.getBookId()):
                found = True
                break

        if not found:
            raise rentalControllerException("Book id not found !!!")

        found = False
        for x in clients:
            if int(x.getId()) == int(r.getClientId()):
                found = True
                break

        if not found:
            raise rentalControllerException("Client id not found !!!")

        self.__rentalRepository.addItem(r)


    def return_book(self, arg):

        found = False
        rentals = self.__rentalRepository.getItems()
        for x in rentals:
            if int(x.getBookId()) == int(arg):
                found = True
                r = rental(x.getId(), x.getBookId(), x.getClientId(), x.getRentedDate(), x.getDueDate(), time.strftime("%d/%m/%Y"))
                self.__rentalRepository.updateItem(r)
        if not found:
            raise rentalControllerException("You can't return a book which was not rented !!!")

    def get_rentals(self):
        return self.__rentalRepository.getItems()

    def remove_rental(self, id):
        self.__rentalRepository.removeItem(id)

    '''
    STATS
    '''

    def most_rented_books(self):
        l = []

        rentedBooks = []
        rentals = self.__rentalRepository.getItems()
        books = self.__bookRepository.getItems()

        for x in rentals:
            rentedBooks.append(x.getBookId())

        rentedBooks = Counter(rentedBooks)
        rentedBooks = sorted(rentedBooks.items(), key=operator.itemgetter(0), reverse=True)

        for x, y in rentedBooks:
            for book in books:
                if int(x) == int(book.getId()):
                    l.append([(str(book.getTitle())), str(book.getId())])

        return l


    def most_active_clients(self):
        rentals = self.__rentalRepository.getItems()

        maxClientId = 0
        for x in rentals:
            maxClientId = max(maxClientId, x.getClientId())

        l = [(0,0) for x in range(maxClientId + 1)]

        for x in rentals:
            if x.getReturnedDate() != "-":
                diff = tools.getDistanceInDays(x.getRentedDate(), x.getReturnedDate())
                l[int(x.getClientId())] = ((int(x.getClientId()), l[int(x.getClientId())][1] + diff))

        l = sorted(l, key = lambda tup: tup[1], reverse = True)
        return l


    def most_rented_authors(self):
        l = []
        rentedAuthors = []
        rentals = self.__rentalRepository.getItems()
        books = self.__bookRepository.getItems()

        for x in rentals:
            id = x.getBookId()
            for y in books:
                if (int(id) == int(y.getId())):
                    rentedAuthors.append(y.getAuthor())

        rentedAuthors = Counter(rentedAuthors)
        rentedAuthors = sorted(rentedAuthors.items(), key=operator.itemgetter(0), reverse=True)

        for x, y in rentedAuthors:
            l.append([str(x), str(y)])

        return l


    def late_rentals(self):
        rentals = self.__rentalRepository.getItems()

        maxBookId = 0
        for x in rentals:
            maxBookId = max(maxBookId, x.getBookId())

        l = [(0, 0) for x in range(maxBookId + 1)]

        for x in rentals:
            if x.getReturnedDate() != "-":
                diff = tools.getDistanceInDays(x.getDueDate(), time.strftime("%d/%m/%Y"))
                if diff > 0:
                    l[int(x.getBookId())] = ((int(x.getBookId()), l[int(x.getBookId())][1] + diff))

        l = sorted(l, key=lambda tup: tup[1], reverse=True)
        return l







