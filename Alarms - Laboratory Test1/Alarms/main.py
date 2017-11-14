from UI import *
from test import *

def cmdScan():
    '''

    :return: command splitted
    '''
    return input("->").split()

def executeCommand(cmd, alarme):
    '''
    check if a valid command and sends data to UI
    '''

    if (cmd[0] == "add"):
        try:
            uiExecuteAdd(cmd, alarme)
        except ValueError as ve:
            print(ve)

    elif (cmd[0] == "print" and len(cmd) == 1):
        try :
            uiExecutePrint(cmd, alarme)
        except ValueError as ve:
            print(ve)

    elif (cmd[0] == "delay"):
        try:
            uiExecuteDelay(cmd, alarme)
        except ValueError as ve:
            print(ve)

    elif (cmd[0] == "delete"):
        try:
            uiExecuteDelete(cmd, alarme)
        except ValueError as ve:
            print(ve)
    else:
        print ("Invalid command")


def start():

    alarme = initialList()

    while True:
        cmd = cmdScan()
        if len(cmd) > 0:
            executeCommand(cmd, alarme)

#startTests()
start()
