from raiseEx import raiseException


class console:
    def __init__(self, controller):
        self.__controller = controller

        self.__functions = [["1", self.addDna, 1], ["2", self.filterDna, 1], ["3", self.sortLongestRepearing, 0], ["4", self.show, 0]]

    #SHOW A SIMPLE MENU
    def uiMenu(self):
        print("\n=========CMDS=========")
        print("1.add DNA")
        print("2.filter subDNA")
        print("3.sort DNA by longest repating")
        print("(DEBUG) 4.show dna")

    #ADD DNA TO THE LIST
    def addDna(self, param):
        self.__controller.addDna(param)


    #FILTER DNA BY SEQUENCE, SORTED BY THE DNA LENGTH
    def filterDna(self, param):
        l = self.__controller.filterDna(param)
        for x in l:
            print (x)

    #PRINT DNA BY LONGEST REPEATING SAME LETTER SEQUENCE
    def sortLongestRepearing(self):
        l = self.__controller.sortLongestRepe()
        for x in l:
            print (x)

    #SHOW ALL THE RECORDS
    def show(self):
        self.__controller.show()

    #SIMPLE IMPUT DATA
    def data(self):
        self.__controller.addDna("TGA")
        self.__controller.addDna("TGGGA")
        self.__controller.addDna("TGTTA")
        self.__controller.addDna("TGAAA")
        self.__controller.addDna("TTTGCCCA")

    #READ AND CHECK THE COMMANDS
    def run(self):
        #self.data()

        while True:
            self.uiMenu()
            line = input("Cmd no -> ").split()

            good_command = False

            if (len(line) == 1):
                for index in self.__functions:
                    if index[0] == line[0]:
                        good_command = True


                        if index[2] != 0:
                            lineCommand = input("Parameters: ").split()

                            if len(lineCommand) == index[2]:
                                try:
                                    if len(lineCommand) == 1:
                                        index[1](lineCommand[0])
                                    else:
                                        index[1](lineCommand)
                                except raiseException as ve:
                                    print(ve)
                            else:
                                good_command = False
                        else:
                            try:
                                index[1]()
                            except raiseException as ve:
                                print(ve)

            if not good_command:
                print("Invalid cmd !")