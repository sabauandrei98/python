from domain.point import point
from textColor import setTextColor
from validation.validation import validator

class repository:

    def __init__(self):
        self.__map = [['=' for x in range(8)] for y in range(8)]

    def markOnMap(self, x, y, symbol, emptySymbol):
        for i in range(int(x) - 1, int(x) + 2):
            for j in range(int(y) - 1, int(y) + 2):
                if validator.pointOnMap(i, j):
                    if (self.__map[i][j] == emptySymbol):
                        self.__map[i][j] = str(point(i, j, symbol))

    def getPointSymbol(self, x, y):
        return self.__map[int(x)][int(y)]

    def getMap(self):
        return self.__map[:]

    def getEmptyPoints(self, emptySymbol):
        points = 0
        for x in self.__map:
            for y in x:
                if y == emptySymbol:
                    points += 1

        return points

    def clearMap(self, emptySymbol):
        self.__map = [[emptySymbol for x in range(8)] for y in range(8)]

    def __str__(self):
        repo = "   "
        k = 0
        l = []

        for x in self.__map:
            repo += setTextColor(1, 31, 38, str(k))
            k += 1

        repo += '\n'
        k = 0

        for x in self.__map:
            repo += setTextColor(1, 31, 38, str(k))
            for y in x:
                if y == 'X':
                    repo += setTextColor(1, 33, 38, y)
                elif y == 'O':
                    repo += setTextColor(1, 35, 38, y)
                elif y == '=':
                    repo += setTextColor(1, 34, 38, y)
            k += 1
            repo += '\n'

        return repo