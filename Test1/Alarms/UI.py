from functionalities import *
from validation import *

def uiExecuteAdd(cmd, alarme):
    checkAdd(cmd)
    executeAdd(cmd, alarme)

def uiExecuteDelay(cmd, alarme):
    checkDelay(cmd)
    executeDelay(cmd, alarme)

def uiExecuteDelete(cmd, alarme):
    checkDelete(cmd)
    executeDelete(cmd, alarme)

def uiExecutePrint(cmd, alarme):
    for x in alarme:
        print(x)