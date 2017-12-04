class book:

    def __init__(self, bookId, title, description, author):
        self.__bookId = bookId
        self.__title = title
        self.__description = description
        self.__author = author


    '''Setters'''
    def setId(self, bookId):
        self.__bookId = bookId
    def setTitle(self, title):
        self.__title = title
    def setDescription(self, description):
        self.__description = description
    def setAuthor(self, author):
        self.__author = author

    '''Getters'''
    def getId(self):
        return self.__bookId
    def getTitle(self):
        return self.__title
    def getDescription(self):
        return self.__description
    def getAuthor(self):
        return self.__author

    def __add__(self, other):
        return other + str(self)

    def __str__(self):
        return (" Id: " + str(self.getId()) +
                " Name: " + str(self.getTitle()) +
                " Description: " + str(self.getDescription()) +
                " Author: " + str(self.getAuthor()))

