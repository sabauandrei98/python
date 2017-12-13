from exceptions.exceptions import raiseException
from undo.undoController import FunctionCall, Operation
from utils import tools


class console():

    def __init__(self, booksController, clientsController, rentalController, undoController):
        print("Console Init")
        self.__booksController = booksController
        self.__clientsController = clientsController
        self.__rentalController = rentalController
        self.__undoController = undoController
        self.__functionHelp = {
            1: "<bookId> <title> <description> <author>",
            2: "<bookId>",
            3: "<bookId> <title> <description> <author>",
            4: "Listing..",
            5: "<bookId> or <title> or <description> or <author>",
            6: "<rentalId> <bookId> <clientId> <dueDate>",
            7: "<bookId>",

            8: "<clientId> <clientName>",
            9: "<clientId>",
            10: "<clientId> <clientName>",
            11: "Listing..",
            12: "<clientId> or <clientName>",

            13: "Most rented books...",
            14: "Most active clients...",
            15: "Most rented author...",
            16: "Late rentals...",
            17: "Undo...",
            18: "Redo...",
        }

        self.__functions = [
                            ["1", self.__functionHelp[1], self.uiAddBook, 4],
                            ["2", self.__functionHelp[2], self.uiRemoveBook, 1],
                            ["3", self.__functionHelp[3], self.uiUpdateBook, 4],
                            ["4", self.__functionHelp[4], self.uiListBooks, 0],
                            ["5", self.__functionHelp[5], self.uiSearchBook, 1],
                            ["6", self.__functionHelp[6], self.uiRentBook, 4],
                            ["7", self.__functionHelp[7], self.uiReturnBook, 1],

                            ["8", self.__functionHelp[8], self.uiAddClient, 2],
                            ["9", self.__functionHelp[9], self.uiRemoveClient, 1],
                            ["10", self.__functionHelp[10], self.uiUpdateClient, 2],
                            ["11", self.__functionHelp[11], self.uiListClients, 0],
                            ["12", self.__functionHelp[12], self.uiSearchClient, 1],

                            ["13", self.__functionHelp[13], self.uiMostRentedBooks, 0],
                            ["14", self.__functionHelp[14], self.uiMostActiveClients, 0],
                            ["15", self.__functionHelp[15], self.uiMostRentedAuthor, 0],
                            ["16", self.__functionHelp[16], self.uiLateRentals, 0],


                            ["17", self.__functionHelp[17], self.uiUndo, 0],
                            ["18", self.__functionHelp[18], self.uiRedo, 0],

                            #EXTRA
                            ["lr", self.__functionHelp[11], self.uiListRentals, 0]]


    def InputData(self):
        self.uiAddBook([1, "andrei1", "andrei1", "andrei1"])
        self.uiAddBook([2, "andrei2", "andrei2", "andrei2"])
        self.uiAddBook([3, "andrei3", "andrei3", "andrei3"])
        self.uiAddBook([4, "andrei4", "andrei4", "andrei4"])
        self.uiAddBook([5, "andrei5", "andrei5", "andrei5"])
        self.uiAddBook([6, "andrei6", "andrei6", "andrei6"])
        self.uiAddBook([7, "andrei7", "andrei7", "andrei7"])
        self.uiAddBook([8, "andrei8", "andrei8", "andrei8"])
        self.uiAddBook([9, "andrei9", "andrei9", "andrei9"])
        self.uiAddBook([10, "andrei10", "andrei10", "andrei10"])
        self.uiAddBook([11, "andrei11", "andrei11", "andrei11"])
        self.uiAddBook([12, "andrei12", "andrei12", "andrei12"])
        self.uiAddBook([13, "andrei13", "andrei13", "andrei13"])
        self.uiAddBook([14, "andrei14", "andrei14", "andrei14"])

        self.uiAddClient([1, "andrei1"])
        self.uiAddClient([2, "andrei2"])
        self.uiAddClient([3, "andrei3"])
        self.uiAddClient([4, "andrei4"])
        self.uiAddClient([5, "andrei5"])
        self.uiAddClient([6, "andrei6"])
        self.uiAddClient([7, "andrei7"])
        self.uiAddClient([8, "andrei8"])

        self.uiRentBook([1, 1, 1, "7/12/2017", "12/12/2017", "-"])
        self.uiRentBook([2, 2, 1, "7/12/2017", "12/12/2017", "-"])
        self.uiRentBook([3, 3, 2, "7/12/2017", "12/12/2017", "-"])
        self.uiRentBook([4, 4, 2, "7/12/2017", "12/12/2017", "-"])
        self.uiRentBook([5, 5, 2, "7/12/2017", "12/12/2017", "10/12/2017"])
        self.uiRentBook([6, 6, 2, "7/12/2017", "12/12/2017", "10/12/2017"])
        self.uiRentBook([7, 7, 3, "7/12/2017", "12/12/2017", "-"])
        self.uiRentBook([8, 8, 3, "7/12/2017", "12/12/2017", "-"])
        self.uiRentBook([9, 9, 3, "7/12/2017", "12/12/2017", "-"])
        self.uiRentBook([10, 10, 3, "7/12/2017", "12/12/2017", "-"])


    '''
    BOOKS
    '''

    #CRUD
    def uiAddBook(self, arg):
        self.__booksController.add_book(arg)

        self.__undoController.newOperation()
        redo = FunctionCall(self.uiAddBook, arg)
        undo = FunctionCall(self.uiRemoveBook, arg[0])
        operation = Operation(undo, redo)
        self.__undoController.recordOperation(operation)

    def uiRemoveBook(self, arg):
        tools.isInt(arg[0])
        b = self.__booksController.getItem(arg)

        self.__booksController.remove_book(arg)

        self.__undoController.newOperation()
        redo = FunctionCall(self.uiRemoveBook, arg)
        undo = FunctionCall(self.uiAddBook, [b.getId(), b.getTitle(), b.getDescription(), b.getAuthor()])
        operation = Operation(undo, redo)
        self.__undoController.recordOperation(operation)

    def uiUpdateBook(self, arg):
        tools.isInt(arg[0])
        b = self.__booksController.getItem(arg[0])

        self.__booksController.update_book(arg)

        self.__undoController.newOperation()
        redo = FunctionCall(self.uiUpdateBook, arg)
        undo = FunctionCall(self.uiUpdateBook, [b.getId(), b.getTitle(), b.getDescription(), b.getAuthor()])
        operation = Operation(undo, redo)
        self.__undoController.recordOperation(operation)

    def uiListBooks(self):
        books = self.__booksController.get_books()
        for x in books:
            print(x)

    #EXTRA
    def uiSearchBook(self, arg):
        found = self.__booksController.search_book(arg)
        for x in found:
            print (x + "Found:")


    '''
    CLIENTS
    '''

    #CRUD
    def uiAddClient(self, arg):
        self.__clientsController.add_client(arg)

        self.__undoController.newOperation()
        redo = FunctionCall(self.uiAddClient, arg)
        undo = FunctionCall(self.uiRemoveClient, arg[0])
        operation = Operation(undo, redo)
        self.__undoController.recordOperation(operation)

    def uiRemoveClient(self, arg):
        tools.isInt(arg[0])
        c = self.__clientsController.getItem(arg)

        self.__clientsController.remove_client(arg)

        self.__undoController.newOperation()
        redo = FunctionCall(self.uiRemoveClient, arg)
        undo = FunctionCall(self.uiAddClient, [c.getId(), c.getName()])
        operation = Operation(undo, redo)
        self.__undoController.recordOperation(operation)

    def uiUpdateClient(self, arg):
        tools.isInt(arg[0])
        c = self.__clientsController.getItem(arg[0])

        self.__clientsController.update_client(arg)

        self.__undoController.newOperation()
        redo = FunctionCall(self.uiUpdateClient, arg)
        undo = FunctionCall(self.uiUpdateClient, [c.getId(), c.getName()])
        operation = Operation(undo, redo)
        self.__undoController.recordOperation(operation)

    def uiListClients(self):
        clients = self.__clientsController.get_clients()
        for x in clients:
            print(x)

    #EXTRA
    def uiSearchClient(self, arg):
        found = self.__clientsController.search_client(arg)
        for x in found:
            print (x + "Found:")

    '''
    RENTALS
    '''

    def uiRentBook(self, arg):
        self.__rentalController.rent_book(arg)

        self.__undoController.newOperation()
        redo = FunctionCall(self.uiRentBook, arg)
        undo = FunctionCall(self.__rentalController.remove_rental, arg[0])
        operation = Operation(undo, redo)
        self.__undoController.recordOperation(operation)

    def uiReturnBook(self, arg):
        self.__rentalController.return_book(arg)

        self.__undoController.newOperation()
        redo = FunctionCall(self.uiReturnBook, arg)
        undo = FunctionCall(self.__rentalController.cancel_rental, arg)
        operation = Operation(undo, redo)
        self.__undoController.recordOperation(operation)

    def uiListRentals(self):
        rentals = self.__rentalController.get_rentals()
        for x in rentals:
            print(x)

    '''
    STATS
    '''

    def uiMostRentedBooks(self):
        most_rented = self.__rentalController.most_rented_books()
        for x in most_rented:
            print ("Book: " + str(x[0]) + " Rentals: " + str([1]))

    def uiMostActiveClients(self):
        most_active = self.__rentalController.most_active_clients()
        for x in most_active:
            if x[1] != 0:
                print ("Client id: " + str(x[0]) + " Days: " + str(x[1]))

    def uiMostRentedAuthor(self):
        rented_authors = self.__rentalController.most_rented_authors()
        for x in rented_authors:
            print ("Author: " + str(x[0]) + " Rentals: " + str(x[1]))

    def uiLateRentals(self):
        late_rentals = self.__rentalController.late_rentals()
        for x in late_rentals:
            if x[1] != 0:
                print("Book id: " + str(x[0]) + " Days: " + str(x[1]))

    '''
    UNDO/REDO
    '''
    def uiUndo(self):
        self.__undoController.undo()

    def uiRedo(self):
        self.__undoController.redo()


    '''
    MENU
    '''

    def uiMenu(self):
        print("\n\n=========INPUT=========")
        print("Date format must be: DD/MM/YYYY")
        print("<title>, <description>, <author> must have length 1")

        print("=========MENU=========")
        print("=========BOOKS=========")
        print("1. Add book   || 2. Delete book || 3. Update book" )
        print("4. List books || 5. Search book || 6. Rent book   || 7. Return book")

        print("=========CLIENTS=========")
        print("8. Add client    || 9. Delete client || 10. Update client")
        print("11. List clients || 12. Search client")

        print("=========STATS=========")
        print("13. Most rented books   || 14. Most active clients")
        print("15. Most rented authors || 16. Late rentals")

        print("=========CHANGE_DATA=========")
        print("17. Undo || 18. Redo")

        print("=========EXTRA=========")
        print("lr. List rentals\n")


    def showMenu(self):
        print("==========================")
        print ("Welcome to the library !")
        print("==========================")

    def run(self):
        self.showMenu()
        #self.InputData()


        while True:
            self.uiMenu()
            line = input("Command number -> ").split()

            good_command = False

            if (len(line) == 1):
                for index in self.__functions:
                    if index[0] == line[0]:
                        good_command = True

                        if index[3] != 0:
                            print(index[1])
                            lineCommand = input("Params: ").split()

                            if len(lineCommand) == index[3]:
                                try:
                                    if len(lineCommand) == 1:
                                        index[2](lineCommand[0])
                                    else:
                                        index[2](lineCommand)
                                except raiseException as ve:
                                    print(ve)
                            else:
                                good_command = False
                        else:
                            print(index[1])
                            try:
                                index[2]()
                            except raiseException as ve:
                                print(ve)

            if not good_command:
                print("Invalid command !!!")

