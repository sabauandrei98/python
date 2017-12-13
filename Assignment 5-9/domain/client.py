class client:

    def __init__(self, clientId, name):
        self.__clientId = clientId
        self.__name = name

    '''Setters'''
    def setId(self, clientId):
        self.__clientId = clientId
    def setName(self, name):
        self.__name = name

    '''Getters'''
    def getId(self):
        return self.__clientId
    def getName(self):
        return self.__name

    def __add__(self, other):
        return other + str(self)

    def __str__(self):
        return (" Id: " + str(self.getId()) +
                " Name: " + str(self.getName()))