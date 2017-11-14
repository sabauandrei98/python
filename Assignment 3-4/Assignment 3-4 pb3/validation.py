from utils import*

#tested
def checkAddCommand(cmd):

    error = ""
    if (len(cmd) != 3):
        error += "Invalid command format (add <sum> <category>) ! \n"

    if (len(cmd) > 1):
        if (isInt(cmd[1]) == False):
            error += "Invalid <sum> ! \n"

    if (len(cmd) > 2):
        if (isCategory(cmd[2]) == False):
            error += "Invalid <category> ! \n"

    if (len(error) > 0):
        raise ValueError(error)

#tested
def checkInsertCommand(cmd):

    error = ""
    if (len(cmd) != 4):
        error += "Invalid command format (insert <day> <sum> <category>) ! \n"

    if (len(cmd) > 1):
        if (isDay(cmd[1]) == False):
            error += "Invalid <day> ! \n"

    if (len(cmd) > 2):
        if (isInt(cmd[2]) == False):
            error += "Invalid <sum> ! \n"

    if (len(cmd) > 3):
        if (isCategory(cmd[3]) == False):
            error += "Invalid <category> ! \n"

    if (len(error) > 0):
        raise ValueError(error)

#tested
def checkValueFilterCommand(cmd):

    error = ""
    if (isCategory(cmd[1]) == False):
        error += "Invalid <category> ! \n"

    if (isOperator(cmd[2]) == False):
        error += "Invalid <operator> ! \n"

    if (isInt(cmd[3]) == False):
        error += "Invalid <sum> ! \n"

    if (len(error) > 0):
        raise ValueError(error)

#tested
def checkCategoryFilterCommand(cmd):

    error = ""
    if (isCategory(cmd[1]) == False):
        error += "Invalid <category> ! \n"

    if (len(error) > 0):
        raise ValueError(error)

#tested
def checkSumCommand(cmd):

    error = ""
    if (len(cmd) != 2):
        error += "Invalid command format (sum <category>) ! \n"

    if (len(cmd) > 1):
        if (isCategory(cmd[1]) == False):
            error += "Invalid <category> ! \n"

    if (len(error) > 0):
        raise ValueError(error)

#tested
def checkMaxCommand(cmd):

    error = ""
    if (len(cmd) != 2):
        error += "Invalid command format (max <day>) ! \n"

    if (len(cmd) > 1):
        if (isDay(cmd[1]) == False):
            error += "Invalid <day> ! \n"

    if (len(error) > 0):
        raise ValueError(error)

#tested
def checkSortCommand(cmd):

    error = ""
    if (len(cmd) < 2):
        error += "Invalid command format (sort <day>)! \n"

    if (len(cmd) > 1):
        if (isDay(cmd[1]) == False and isCategory(cmd[1]) == False):
            error += "Invalid <day>/<category> ! \n"

    if (len(error) > 0):
        raise ValueError(error)

#tested
def checkValueListCommand(cmd):

    error = ""
    if (isCategory(cmd[1]) == False):
        error += "Invalid <category> ! \n"

    if (isOperator(cmd[2]) == False):
        error += "Invalid <operator> ! \n"

    if (isInt(cmd[3]) == False):
        error += "Invalid <sum> ! \n"

    if (len(error) > 0):
        raise ValueError(error)

#tested
def checkCategoryListCommand(cmd):

    error = ""
    if (isCategory(cmd[1]) == False):
        error += "Invalid <category> ! \n"

    if (len(error) > 0):
        raise ValueError(error)

#tested
def checkIntervalRemoveCommand(cmd):

    error = ""
    if (isDay(cmd[1]) == False or isDay(cmd[3]) == False):
        error += "Invalid <day> ! \n"
    else:
        if (int(cmd[1]) > int(cmd[3])):
            error += "Invalid interval format ! \n"

    if (cmd[2] != 'to'):
        error += "Invalid command format ! \n"

    if (len(error) > 0):
        raise ValueError(error)

#tested
def checkNormalRemoveCommand(cmd):

    error = ""
    if (isDay(cmd[1]) == False and isCategory(cmd[1]) == False):
        error += "Invalid <day>/<category> ! \n"

    if (len(error) > 0):
        raise ValueError(error)

#tested
def checkUndoCommand(undoList, cmd):

    error = ""
    if (len(cmd) != 1):
        error += "Invalid command format (undo) ! \n"

    if (len(undoList) == 0):
        error += "Nothing to undo ! \n"

    if (len(error) > 0):
        raise ValueError(error)