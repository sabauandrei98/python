from random import randint
from exceptions import raiseException

class controler:

    def __init__(self, repository):
        self.__repositoy = repository

    def getMap(self):
        return self.__repositoy.getMap()

    def clearMap(self, emptySymbol):
        self.__repositoy.clearMap(emptySymbol)

    def printMap(self):
        return self.__repositoy

    def movePlayer(self, x, y, symbol, emptySymbol):
        if self.__repositoy.getPointSymbol(x, y) != emptySymbol:
            raise raiseException("Overlapping points !!!")
        self.__repositoy.markOnMap(x, y, symbol, emptySymbol)

    def moveAI(self, symbol, emptySymbol):
        l = []
        mapCopy = self.__repositoy.getMap()

        for x in range(0, 8):
            for y in range (0, 8):
                if mapCopy[x][y] == emptySymbol:
                    l.append((x, y))

        print (l)
        if len(l) > 0:
            print("MOVE AI...")
            r = randint(0, len(l) - 1)
            self.__repositoy.markOnMap(l[r][0], l[r][1], symbol, emptySymbol)
        print('\n' + str(len(l)))

    def getEmptyPoints(self, emptySymbol):
        return self.__repositoy.getEmptyPoints(emptySymbol)