class rental:

    def __init__(self, rentalId, bookId, clientId, rentedDate, dueDate, returnedDate):
        self.__rentalId = rentalId
        self.__bookId = bookId
        self.__clientId = clientId
        self.__rentedDate = rentedDate
        self.__dueDate = dueDate
        self.__returnedDate = returnedDate

    '''Getters'''
    def getId(self):
        return self.__rentalId
    def getBookId(self):
        return self.__bookId
    def getClientId(self):
        return self.__clientId
    def getRentedDate(self):
        return self.__rentedDate
    def getDueDate(self):
        return self.__dueDate
    def getReturnedDate(self):
        return self.__returnedDate

    '''Setters'''
    def setId(self, rentalId):
        self.__rentalId = rentalId
    def setBookId(self, bookId):
        self.__bookId = bookId
    def setClientId(self, clientId):
        self.__clientId = clientId
    def setRentedDate(self, rentedDate):
        self.__rentedDate = rentedDate
    def setDueDate(self, dueDate):
        self.__dueDate = dueDate
    def setReturnedDate(self, returnedDate):
        self.__returnedDate = returnedDate

    def __add__(self, other):
        return other + str(self)

    def __str__(self):
        return (" Id: " + str(self.getId()) +
                " bookId: " + str(self.getBookId()) +
                " clientId: " + str(self.getClientId()) +
                " rentedDate: " + str(self.getRentedDate()) +
                " dueDate: " + str(self.getDueDate()) +
                " returnedDate: " + str(self.getReturnedDate()))





