class point:

    def __init__(self, x, y, symbol):
        self.__symbol = symbol
        self.__x = x
        self.__y = y

    def setSymbol(self, symbol):
        self.__symbol = symbol

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getSymbol(self):
        return self.__symbol

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def __str__(self):
        return self.__symbol