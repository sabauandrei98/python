from exceptions import raiseException
from validation.validation import validator
from textColor import setTextColor

class console:

    def __init__(self, controler, maxX, maxY):
        self.__controler = controler
        self.__play = True
        self.__playerSymbol = "X"
        self.__AISymbol = "O"
        self.__emptySymbol = "="
        self.__maxX = maxX
        self.__maxY = maxY

    def mainMenu(self):
        print (setTextColor(1, 32, 38, "Welcome to XMX"))
        print (setTextColor(1, 32, 38, "Grid size: " + str(self.__maxX) + "x" + str(self.__maxY) + "(indexed from 0)\n"))


    def playGame(self):

        print(self.__controler.printMap())
        while self.__play:

            try:
                cmd = input("(X,Y): ").split()

                validator.checkInput(cmd, self.__maxX, self.__maxY)
                self.__controler.movePlayer(cmd[0], cmd[1], self.__playerSymbol, self.__emptySymbol)
                if self.__controler.getEmptyPoints(self.__emptySymbol) == 0:
                    self.gameOver("Player")
                    self.__play = False
                    continue

                self.__controler.moveAI(self.__AISymbol, self.__emptySymbol)
                if self.__controler.getEmptyPoints(self.__emptySymbol) == 0:
                    self.gameOver("AI")
                    self.__play = False
                    continue

                print(self.__controler.printMap())

            except raiseException as ve:
                print(ve)

        cmd = input("cmd: ").split()
        while len(cmd) != 1 and cmd[0] != "/r":
            pass


    def getEmptyPoints(self, emptySymbol):
        return self.__controler.getEmptyPoints(emptySymbol)

    def gameOver(self, player):
        print(setTextColor(1, 36, 38, player + " wins !"))

    def startGame(self):
        self.mainMenu()
        self.playGame()



