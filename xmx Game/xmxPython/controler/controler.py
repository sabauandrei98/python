from random import randint

from copy import deepcopy

from domain.point import point
from exceptions import raiseException
from validation.validation import validator


class controler:

    def __init__(self, repository):
        self.__repositoy = repository
        self.__coordsFreq = []
        self.__coordsCount = 0
        self.__aux_coords = ""

        for i in range(0, 100):
            self.__coordsFreq.append(0)

    def getMap(self):
        return self.__repositoy.getMap()


    def printMap(self):
        return self.__repositoy

    def movePlayer(self, x, y, symbol, emptySymbol):
        if self.__repositoy.getPointSymbol(x, y) != emptySymbol:
            raise raiseException("Overlapping points !!!")
        self.__repositoy.markOnMap(x, y, symbol, emptySymbol)

    def getEmptyPoints(self, emptySymbol):
        return self.__repositoy.getEmptyPoints(emptySymbol)

    def moveAI(self, symbol, emptySymbol):
        l = []
        mapCopy = self.__repositoy.getMap()

        maxCoords = self.__repositoy.getXY()

        if self.__repositoy.getEmptyPoints(emptySymbol) >= 80:
            point = self.getPoint(mapCopy)
            print(point)
            self.__repositoy.markOnMap(point[0], point[1], symbol, emptySymbol)
        else:
            for x in range(0, maxCoords[0]):
                for y in range (0, maxCoords[1]):
                    if mapCopy[x][y] == emptySymbol:
                        l.append((x, y))

            if len(l) > 0:
                print("MOVE AI...")
                r = randint(0, len(l) - 1)
                self.__repositoy.markOnMap(l[r][0], l[r][1], symbol, emptySymbol)


    ##############################################################################


    def resetCoords(self):
        for i in range(0, 100):
            self.__coordsFreq[i] = 0
        self.__coordsCount = 0


    def getPoint(self, board):
        self.resetCoords()
        self.searchForMove(board)

        best = 0
        point = []
        for i in range(1, 100):
            if (self.__coordsFreq[i] > best):
                print ("da")
                best = self.__coordsFreq[i]
                point = (int(i / 10), i % 10)

        return point

    def isMapFull(self, board):
        maxCoords = self.__repositoy.getXY()
        for x in range(0, maxCoords[0]):
            for y in range(0, maxCoords[1]):
                if board[x][y] == "=":
                    return False
        return True

    def markOnMap(self, x, y, board, symbol):
        maxCoords = self.__repositoy.getXY()
        for i in range(int(x) - 1, int(x) + 2):
            for j in range(int(y) - 1, int(y) + 2):
                if validator.pointOnMap(i, j, maxCoords[0], maxCoords[1]):
                    if (board[i][j] == "="):
                        board[i][j] = str(point(i, j, symbol))

    def searchForMove(self, board, coords = ""):

        if (self.__coordsCount > 10):
            return

        if (self.isMapFull(board) == False):
            maxCoords = self.__repositoy.getXY()
            for i in range(0, maxCoords[0]):
                for j in range(0, maxCoords[1]):
                    if (board[i][j] == "="):

                        auxBoard = deepcopy(board)
                        self.markOnMap(i, j, auxBoard, "O")

                        if coords == "":
                            self.__aux_coords = str(i) + " " + str(j)



                        if (self.isMapFull(auxBoard) == True):
                            self.__coordsCount += 1
                            self.__coordsFreq[i*10 + j] += 1
                            return
                        else:
                            for ii in range(i+1, maxCoords[0]):
                                for jj in range(j+1, maxCoords[1]):
                                    if (auxBoard[ii][jj] == "="):
                                        auxBoard2 = deepcopy(board)
                                        self.markOnMap(ii, jj, auxBoard2, "X")

                                        self.searchForMove(auxBoard2, self.__aux_coords)
        else:
            i = int(coords[0])
            j = int(coords[2])
            self.__coordsFreq[i * 10 + j] -= 1
