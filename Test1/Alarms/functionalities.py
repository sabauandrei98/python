from domain import *

def executeAdd(cmd, alarme):
    alarme.append (createAlarm(cmd[1], cmd[2], cmd[3], cmd[4]))
    return alarme

def executeDelay(cmd, alarme):
    for x in alarme:
        if equal(x[0], x[1], x[2], cmd[1], cmd[2], cmd[3]):
            time = addTime(x[0], x[1], x[2], cmd[4], cmd[5], cmd[6])
            if (time[0] > 24):
                return False
            else:
                alarme.pop(alarme.index(x))
                alarme.append((time[0], time[1], time[2], x[3]))
    return alarme


def executeDelete(cmd, alarme):

    length = 0

    t1 = int(cmd[1]) * 3600 + int(cmd[2]) * 60 + int(cmd[3])
    t2 = int(cmd[4]) * 3600 + int(cmd[5]) * 60 + int(cmd[6])

    while len(alarme) != length:
        length = len(alarme)
        for i in alarme:

            x = int(i[0]) * 3600 + int(i[1]) * 60 + int(i[2])
            if (x >= t1 and x <= t2):
                alarme.pop(alarme.index(i))

    return alarme
