from utils import*

def checkAdd(cmd):
    '''
    validates if Add command is in correct format
    '''

    error = ""

    if (len(cmd) != 5):
        error += "Invalid command format! \n"
    else:
        if (isTime(cmd[1], cmd[2], cmd[3]) == False):
            error += "Invalid time format! \n"

    if (len(error) > 0):
        raise ValueError(error)

def checkDelay(cmd):
    '''
    validates if Delay command is in correct format
    '''
    error = ""

    if (len(cmd) != 7):
        error += "Invalid command format! \n"
    else:
        if (isTime(cmd[1], cmd[2], cmd[3]) == False):
            error += "Invalid time format! \n"

        if (isTime(cmd[4], cmd[5], cmd[6]) == False):
            error += "Invalid time format! \n"

    if (len(error) > 0):
        raise ValueError(error)

def checkDelete(cmd):
    '''
    validates if Delete command is in correct format
    '''
    error = ""

    if (len(cmd) != 7):
        error += "Invalid command format! \n"
    else:
        if (isTime(cmd[1], cmd[2], cmd[3]) == False):
            error += "Invalid time format! \n"

        if (isTime(cmd[4], cmd[5], cmd[6]) == False):
            error += "Invalid time format! \n"

    if (len(error) > 0):
        raise ValueError(error)