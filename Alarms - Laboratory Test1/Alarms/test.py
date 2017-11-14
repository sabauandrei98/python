from functionalities import*


def initialList():
    l = []
    l.append((10, 10, 10, "tenis"))
    l.append((15, 10, 10, "tenis"))
    l.append((20, 10, 10, "tenis"))
    l.append((22, 10, 10, "tenis"))
    return l


def startTests():

    #add
    l = []
    cmd = ['add', '5', '5', '5', 'des']
    assert(executeAdd(cmd, l) == [(5, 5, 5, 'des')])

    #delay
    l = []
    l = initialList()
    cmd = ['delay', '10', '10', '10', '1', '1', '1']
    executeDelay(cmd, l)
    assert (l[3] == (11, 11, 11, 'tenis'))

    #delete
    l = []
    l = initialList()
    cmd = ['delete', '10', '10', '10', '20', '20', '20']
    executeDelete(cmd, l)
    assert (l[0] == (22, 10, 10, 'tenis'))





