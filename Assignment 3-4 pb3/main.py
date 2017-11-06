from UI import*
from test import*
from utils import sortTupList

def readCommand():
    '''
    :return: a list containing the items from input
    '''
    return input("Command: ").split()

def sendCommand(expensesList, cmd, undoList):
    '''
    Checks if input contains a semi valid command then
    sends it to the ui to be processed
    '''

    if (len(cmd) == 0):
        print ("No command entered")
        return

    #PROBLEM COMMANDS
    if (cmd[0] == 'add'):
        try:
            undoList.append(expensesList[:])
            uiExecuteAdd(expensesList, cmd)
        except ValueError as ve:
            print(ve)
            undoList.pop()

    elif(cmd[0] == 'insert'):
        try:
            undoList.append(expensesList[:])
            uiExecuteInsert(expensesList, cmd)
        except ValueError as ve:
            print(ve)
            undoList.pop()

    elif (cmd[0] == 'remove'):
        try:
            undoList.append(expensesList[:])
            uiExecuteRemove(expensesList, cmd)
        except ValueError as ve:
            print(ve)
            undoList.pop()

    elif (cmd[0] == 'list'):
        try:
            uiExecuteList(expensesList, cmd)
        except ValueError as ve:
            print(ve)

    elif (cmd[0] == 'sum'):
        try:
            uiExecuteSum(expensesList, cmd)
        except ValueError as ve:
            print(ve)

    elif (cmd[0] == 'max'):
        try:
            uiExecuteMax(expensesList, cmd)
        except ValueError as ve:
            print(ve)

    elif (cmd[0] == 'sort'):
        try:
            uiExecuteSort(expensesList, cmd)
        except ValueError as ve:
            print(ve)

    elif (cmd[0] == 'filter'):
        try:
            undoList.append(expensesList[:])
            uiExecuteFilter(expensesList, cmd)
        except ValueError as ve:
            print(ve)
            undoList.pop()

    elif (cmd[0] == 'undo'):
        try:
            uiExecuteUndo(expensesList, undoList, cmd)
        except ValueError as ve:
            print(ve)

    #EXTRA COMMANDS
    elif (cmd[0] == '/sort' and len(cmd) == 1):
        sortTupList(expensesList, 0)
    elif (cmd[0] == '/ulist' and len(cmd) == 1):
        printList(undoList)
    elif (cmd[0] == '/help' and len(cmd) == 1):
        helpUi()
    else:
        print("This command is invalid ! \nType: /help for instructions")

def start():
    '''
    the main part of the program
    - show a simple UI
    - initialization
    - command loop
    '''

    #INITIALIZATION
    uiStart()
    expensesList = testInput()
    undoList = []

    #CMD LOOP
    while True:
        cmd = readCommand()
        uiExecCommand(cmd)
        sendCommand(expensesList, cmd, undoList)

runTests()
start()