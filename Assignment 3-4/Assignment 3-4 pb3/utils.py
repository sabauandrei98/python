#tested
def isInt(n):
    '''
    :param n: any type of data
    :return: True if positive number,
             False otherwise
    '''

    try:
        x = int(n)
        if (x > 0):
            return True
        else:
            return False
    except:
        return False

#tested
def isCategory(n):
    '''
    :param n: any type of data
    :return: True if it represents a category,
             False otherwise
    '''

    if n == "housekeeping" or n == "food" or n == "transport" or n == "clothing" or n == "internet" or n == "others":
        return True
    return False

#tested
def isDay(n):
    '''
    :param n: any type of data
    :return: True if number between 1-30,
             False otherwise
    '''

    try:
        if 1 <= int(n) and int(n) <= 31:
            return True
        else:
            return False
    except:
        return False

#tested
def isOperator(n):
    '''
    :param n: any type of data
    :return: True if <, =, >
             False otherwise
    '''

    if n in ['<', '=', '>']:
        return True
    return False

#tested
def returnDay(n):
    '''
    :param n: string
    :return: n - integer
    ex : input: '02'
         output: 2
    '''

    if n[0] == '0':
        return int(n[1])
    return int(n)

#tested
def sortTupList(l, ind):
    '''
    :param l: list of tuples
    :param ind: on which column to sort the list of tuples
    :return: a sorted list of tuples
    '''

    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][ind] < l[j][ind]:
                l[i], l[j] = l[j], l[i]
    return l

