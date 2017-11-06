from functionalities import*
from validation import*
from utils import*

def testInput():
    l = []
    l.append((1, 50, "transport"))
    l.append((4, 25, "internet"))
    l.append((6, 90, "housekeeping"))
    l.append((9, 120, "food"))
    l.append((10, 10, "transport"))
    l.append((10, 300, "others"))
    l.append((10, 50, "clothing"))
    l.append((10, 23, "food"))
    l.append((10, 80, "internet"))
    l.append((10, 120, "transport"))
    l.append((21, 30, "food"))
    l.append((22, 30, "food"))
    l.append((23, 30, "food"))
    l.append((24, 30, "food"))

    return l

def runTests():
    utilsTest()
    validationTest()
    functionalitiesTest()

def functionalitiesTest():

    #addExpense
    l = []
    l.append((1, 30, "food"))
    cmd = ['add', '2', '3', 'food']
    assert(addExpense(l, cmd) == [(1, 30, 'food'), (2, 3, 'food')])

    l = []
    l.append((1, 30, "food"))
    cmd = ['add', '1', '3', 'food']
    assert(addExpense(l, cmd) == [(1, 33, 'food')])

    #normalRemove
    l = []
    l.append((1, 30, "food"))
    l.append((1, 10, "internet"))
    l.append((3, 20, "food"))
    cmd = ['remove', '1']
    assert (executeNormalRemove(l, cmd) == [(3, 20, "food")])

    #intervalRemove
    l = []
    l.append((1, 30, "food"))
    l.append((2, 10, "internet"))
    l.append((3, 20, "food"))
    l.append((3, 20, "internet"))
    l.append((5, 20, "food"))
    l.append((8, 20, "food"))
    cmd = ['remove', '2', 'to', '5']
    assert (executeIntervalRemove(l, cmd) == [(1, 30, 'food'), (8, 20, "food")])

    #categoryList
    l = []
    l.append((1, 30, "food"))
    l.append((2, 10, "internet"))
    l.append((5, 20, "food"))
    l.append((8, 20, "food"))
    cmd = ['list', 'food']
    assert (executeCategoryList(l, cmd) == [(1, 30, 'food'), (5, 20, "food"), (8, 20, "food")])

    # valueList
    l = []
    l.append((1, 30, "food"))
    l.append((2, 10, "internet"))
    l.append((5, 20, "food"))
    l.append((8, 8, "food"))
    l.append((9, 8, "food"))
    cmd = ['list', 'food', '=', '8']
    assert (executeValueList(l, cmd) == [(8, 8, 'food'), (9, 8, "food")])

    l = []
    l.append((1, 30, "food"))
    l.append((2, 2, "internet"))
    l.append((5, 20, "food"))
    l.append((5, 6, "internet"))
    l.append((8, 8, "food"))
    l.append((9, 8, "food"))
    cmd = ['list', 'internet', '<', '5']
    assert (executeValueList(l, cmd) == [(2, 2, "internet")])

    #executeSum
    l = []
    l.append((1, 30, "food"))
    l.append((2, 2, "internet"))
    l.append((5, 20, "food"))
    l.append((5, 6, "internet"))
    cmd = ['sum', 'internet']
    assert (executeSum(l, cmd) == 8)
    cmd = ['sum', 'food']
    assert (executeSum(l, cmd) == 50)

    #executeMax
    l = []
    l.append((1, 30, "food"))
    l.append((2, 2, "internet"))
    l.append((2, 20, "food"))
    l.append((5, 6, "internet"))
    cmd = ['max', '2']
    assert (executeMax(l, cmd) == 20)

    #executeSort
    l = []
    l.append((1, 30, "food"))
    l.append((2, 2, "internet"))
    l.append((2, 20, "food"))
    cmd = ['sort', 'food']
    assert (executeSort(l, cmd) == [(2, 20, "food"), (1, 30, "food")])

    #executeCategoryFilter
    l = []
    l.append((1, 30, "food"))
    l.append((2, 2, "internet"))
    l.append((2, 20, "food"))
    l.append((5, 30, "food"))
    l.append((6, 2, "others"))
    cmd = ['filter', 'food']
    assert (executeCategoryFilter(l, cmd) == [(1, 30, "food"), (2, 20, "food"), (5, 30, "food")])

    #executeValueFilter
    l = []
    l.append((1, 30, "food"))
    l.append((2, 2, "internet"))
    l.append((2, 20, "food"))
    l.append((5, 30, "food"))
    l.append((6, 2, "others"))
    cmd = ['filter', 'food', '>', '25']
    assert (executeValueFilter(l, cmd) == [(1, 30, "food"), (5, 30, "food")])

    #executeValueFilter
    l = []
    s = []
    ul = []
    l.append((1, 30, "food"))
    l.append((2, 2, "internet"))
    l.append((2, 20, "food"))
    l.append((5, 30, "food"))
    l.append((6, 2, "others"))
    ul.append(l)

    s.append((10, 30, "food"))
    s.append((12, 21, "internet"))
    s.append((15, 25, "clothes"))
    s.append((25, 30, "food"))
    s.append((26, 2, "others"))
    ul.append(s)
    cmd = ['undo']
    assert(executeUndo(ul, cmd) == s)
    assert(executeUndo(ul, cmd) == l)

def validationTest():

    #checkAddCommand
    try:
        checkAddCommand(['add', '5'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid command format (add <sum> <category>) ! \n")

    try:
        checkAddCommand(['add', '5', '5'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid <category> ! \n")

    try:
        checkAddCommand(['add', '5', 'food'])
        assert (True)
    except:
        pass


    #checkInsertCommand
    try:
        checkInsertCommand(['insert', '5'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid command format (insert <day> <sum> <category>) ! \n")

    try:
        checkInsertCommand(['insert', 'food', 'dada', '5'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid <day> ! \nInvalid <sum> ! \nInvalid <category> ! \n")

    try:
        checkInsertCommand(['insert', '5', '5', 'food'])
        assert (True)
    except:
        pass


    #checkValueFilterCommand
    try:
        checkValueFilterCommand(['filter', 'food', '>', 'dsa'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid <sum> ! \n")

    try:
        checkValueFilterCommand(['filter', 'food', '{', '5'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid <operator> ! \n")

    try:
        checkValueFilterCommand(['filter', 'food', '<', '5'])
        assert (True)
    except:
        pass


    #checkSumCommand
    try:
        checkSumCommand(['sum', 'fo'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid <category> ! \n")

    try:
        checkSumCommand(['sum', 'food'])
        assert (True)
    except:
        pass


    #checkMaxCommand
    try:
        checkMaxCommand(['max', 'food'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid <day> ! \n")

    try:
        checkMaxCommand(['max', '10'])
        assert (True)
    except:
        pass

    #checkSortCommand
    try:
        checkSortCommand(['sort', '-412'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid <day>/<category> ! \n")

    try:
        checkSortCommand(['sort', 'innet'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid <day>/<category> ! \n")

    try:
        checkSortCommand(['max', '10'])
        assert (True)
    except:
        pass

    #checkValueList
    try:
        checkValueListCommand(['list', 'f', '>', '3'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid <category> ! \n")

    try:
        checkValueListCommand(['list', 'food', ']', '3'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid <operator> ! \n")

    try:
        checkValueListCommand(['list', 'food', '>', '3'])
        assert (True)
    except:
        pass

    #checkIntervalRemoveCommand
    try:
        checkIntervalRemoveCommand(['remove', '5e', 'to', '10'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid <day> ! \n")

    try:
        checkIntervalRemoveCommand(['remove', '30', 'to', '10'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid interval format ! \n")

    try:
        checkValueListCommand(['list', 'food', '>', '3'])
        assert (True)
    except:
        pass

    #checkUndoCommand
    try:
        l = [(0,0,0)]
        checkUndoCommand(l, ['undo', '5e'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Invalid command format (undo) ! \n")

    try:
        l = []
        checkUndoCommand(l, ['undo'])
        assert (False)
    except ValueError as ve:
        assert(str(ve) == "Nothing to undo ! \n")

    try:
        l = [(0,0,0)]
        checkUndoCommand(l, ['undo'])
        assert (False)
    except:
        pass


def utilsTest():

    #isInt
    assert(isInt(-1) == False)
    assert(isInt(0) == False)
    assert(isInt(1) == True)

    #isCategory
    assert(isCategory('food') == True)
    assert(isCategory('cola') == False)

    #isDay
    assert (isDay('02') == True)
    assert (isDay('10') == True)
    assert (isDay('40') == False)

    #isOperator
    assert (isOperator('+') == False)
    assert (isOperator('<>') == False)
    assert (isOperator('==') == False)
    assert (isOperator('>=') == False)
    assert (isOperator('=') == True)
    assert (isOperator('<') == True)

    #returnDay
    assert (returnDay('02') == 2)
    assert (returnDay('24') == 24)

    #sortTupList
    l = []
    l.append((1,4,3))
    l.append((2,3,2))
    l.append((3,2,1))
    l.append((4,1,4))

    assert (sortTupList(l, 0) == [(1, 4, 3), (2, 3, 2), (3, 2, 1), (4, 1, 4)])
    assert (sortTupList(l, 1) == [(4, 1, 4), (3, 2, 1), (2, 3, 2), (1, 4, 3)])
    assert (sortTupList(l, 2) == [(3, 2, 1), (2, 3, 2), (1, 4, 3), (4, 1, 4)])