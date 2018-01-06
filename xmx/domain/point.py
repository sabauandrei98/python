class point:

    def __init__(self, x, y, symbol):
        self.__symbol = symbol

    def getSymbol(self):
        return self.__symbol

    def __str__(self):
        return self.__symbol