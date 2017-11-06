from validation import*
from utils import sortTupList

#tested
def addExpense(expensesList, cmd):
    '''
    :param expensesList: a list of tuples
    :param cmd: string command parameters
    :return: expensesList after insertion
    '''
    checkInsertCommand(cmd)
    l = expensesList
    for i in range(len(l)):
        if (int(cmd[1]) == int(l[i][0]) and cmd[3] == l[i][2]):
            l[i] = (int(l[i][0]), int(l[i][1]) + int(cmd[2]), l[i][2])
            return l

    l.append((int(cmd[1]), int(cmd[2]), cmd[3]))
    return l

#tested
def executeValueFilter(expensesList, cmd):
    '''
    :param expensesList: a list of tuples
    :param cmd: string command parameters
    :return: list of remaining items after filtering by operators
    '''
    checkValueFilterCommand(cmd)
    l = expensesList
    length = 0
    while len(l) != length:
        length = len(l)
        for item in l:
            ok = False
            if (item[2] == cmd[1]):
                if (cmd[2] == '='):
                    if (int(item[1]) != int(cmd[3])):
                        ok = True
                elif (cmd[2] == '>'):
                    if (int(item[1]) <= int(cmd[3])):
                        ok = True
                elif (cmd[2] == '<'):
                    if (int(item[1]) >= int(cmd[3])):
                        ok = True
            else:
                ok = True

            if (ok == True):
                l.pop(l.index(item))
    return l

#tested
def executeCategoryFilter(expensesList, cmd):
    '''
    :param expensesList: a list of tuples
    :param cmd: string command parameters
    :return: list of remaining items after filtering by category
    '''
    checkCategoryFilterCommand(cmd)
    l = expensesList
    length = 0
    while len(l) != length:
        length = len(l)
        for item in l:
            if (item[2] != cmd[1]):
                l.pop(l.index(item))
    return l

#tested
def executeSum(expensesList, cmd):
    '''
    :param expensesList: a list of tuples
    :param cmd: string command parameters
    :return: sum for all expenses for a category
    '''
    checkSumCommand(cmd)
    sum = 0
    for item in expensesList:
        if item[2] == cmd[1]:
            sum += int(item[1])
    return sum

#tested
def executeMax(expensesList, cmd):
    '''
    :param expensesList: a list of tuples
    :param cmd: string command parameters
    :return: the maximum expense of a <day>
    '''
    checkMaxCommand(cmd)
    best = 0
    for item in expensesList:
        if int(item[1]) > best and int(cmd[1]) == int(item[0]):
            best = int(item[1])

    return best

#tested
def executeSort(expensesList, cmd):
    '''
    :param expensesList: a list of tuples
    :param cmd: string command parameters
    :return: a sorted list by expenses/category
    '''
    checkSortCommand(cmd)

    l = sortTupList(expensesList, 1)
    result = []

    if (isCategory(cmd[1])):
        for item in l:
            if item[2] == cmd[1]:
                result.append(item)
    else:
        for item in l:
            if int(item[0]) == int(cmd[1]):
                result.append(item)

    return result

#tested
def executeValueList(expensesList, cmd):
    '''
    :param expensesList: a list of tuples
    :param cmd: string command parameters
    :return: a list containing only the values that passed the filter
    '''
    checkValueListCommand(cmd)
    l = []
    for item in expensesList:
        if item[2] == cmd[1]:
            if cmd[2] == '<':
                if int(item[1]) < int(cmd[3]):
                    l.append(item)
            if cmd[2] == '=':
                if int(item[1]) == int(cmd[3]):
                    l.append(item)
            if cmd[2] == '>':
                if int(item[1]) > int(cmd[3]):
                    l.append(item)
    return l

#tested
def executeCategoryList(expensesList, cmd):
    '''
    :param expensesList: a list of tuples
    :param cmd: string command parameters
    :return: a list containing only the values that passed the category filter
    '''
    checkCategoryListCommand(cmd)
    l = []
    for item in expensesList:
        if item[2] == cmd[1]:
            l.append(item)
    return l

#tested
def executeNormalRemove(expensesList, cmd):
    '''
    :param expensesList: a list of tuples
    :param cmd: string command parameters
    :return: a list without removed items
    '''
    checkNormalRemoveCommand(cmd)
    l = expensesList
    length = 0
    while len(l) != length:
        length = len(l)
        for i in l:
           if(str(i[0]) == str(cmd[1]) or str(i[2]) == str(cmd[1])):
                l.pop(l.index(i))
    return l

#tested
def executeIntervalRemove(expensesList, cmd):
    '''
    :param expensesList: a list of tuples
    :param cmd: string command parameters
    :return: a list without removed items for a specified interval
    '''
    checkIntervalRemoveCommand(cmd)
    l = expensesList
    length = 0
    while len(l) != length:
        length = len(l)
        for item in l:
            if (int(cmd[1]) <= int(item[0]) and int(item[0]) <= int(cmd[3])):
                l.pop(l.index(item))
    return l

#tested
def executeUndo(undoList, cmd):
    '''
    :param expensesList: a list of tuples
    :param cmd: string command parameters
    :return: a list containing last element of undoList
    '''
    checkUndoCommand(undoList, cmd)

    l = undoList[len(undoList) - 1]
    undoList.pop()
    return l