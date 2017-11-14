from functionalities import*
from datetime import datetime
from validation import*


def uiStart():
    '''
    - a simple UI
    '''
    print ("=== Family expenses ===")
    print (" Extra commands:")
    print (" /help - for help")
    print (" /ulist - print undo list")
    print (" /sort - sort expensesList")
    print ("=======================")

def helpUi():
    '''
    /help command info
    '''
    print("You may use: \n")
    print ("add <sum> <category>")
    print ("insert <day> <sum> <category>")
    print ("remove <day>")
    print ("remove <start day> to <end day>")
    print ("remove <category>")
    print ("list")
    print ("list <category>")
    print ("list <category> [ < | = | > ] <value>")
    print ("sum <category>")
    print ("max <day>")
    print ("sort <day>")
    print ("sort <category>")
    print ("filter <category>")
    print ("filter <category> [ < | = | > ] <value>")
    print ("undo")

def uiExecCommand(cmd):
    print("Executing command... " + str(cmd) + " ")

def uiExecuteAdd(expensesList, cmd):

     if len(cmd) == 3:
        cmd = (cmd[0], int(datetime.now().day), cmd[1], cmd[2])
     addExpense(expensesList, cmd)
     print("Success !!!")

def uiExecuteInsert(expensesList, cmd):

    addExpense(expensesList, cmd)
    print("Success !!!")

def uiExecuteFilter(expensesList, cmd):

    if (len(cmd) == 2):
        executeCategoryFilter(expensesList, cmd)
        print("Success !!!")
    elif (len(cmd) == 4):
        executeValueFilter(expensesList, cmd)
        print("Success !!!")
    else:
        print("Invalid command format  (filter <category>) or (filter <category> [ < | = | > ] <value>) !")

def uiExecuteSum(expensesList, cmd):

    print(executeSum(expensesList, cmd))
    print("Success !!!")

def uiExecuteMax(expensesList, cmd):

    print(executeMax(expensesList, cmd))
    print("Success !!!")

def uiExecuteSort(expensesList, cmd):

    for item in executeSort(expensesList, cmd):
        print(item)
    print("Success !!!")

def uiExecuteList(expensesList, cmd):

    list = []
    if (len(cmd) == 1):
        list = expensesList[:]
    elif (len(cmd) == 2):
        list = executeCategoryList(expensesList, cmd)
    elif (len(cmd) == 4):
        list = executeValueList(expensesList, cmd)
    else:
        print("Invalid command format (list) or (list <category>) or (list <category> [ < | = | > ] <value>)!")
        return

    print("Success !!!")

    #if no warning -> print the list
    printList(list)


def uiExecuteUndo(expensesList, undoList, cmd):

    expensesList[:] = executeUndo(undoList, cmd)
    print("Success !!!")

def uiExecuteRemove(expensesList, cmd):

    if (len(cmd) == 2):
        executeNormalRemove(expensesList, cmd)
        print("Success !!!")
    elif (len(cmd) == 4):
        executeIntervalRemove(expensesList, cmd)
        print("Success !!!")
    else:
        print("Invalid command format (remove <day>) or (remove <start day> to <end day>) or (remove <category>) !")

def printList(l):
    for item in l:
        print(item)
