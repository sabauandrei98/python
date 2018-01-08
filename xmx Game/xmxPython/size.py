from exceptions import raiseException

def printInfo():
    print("Choose size:")
    print("1. 6x5")
    print("2. 6x6")
    print("3. 7x6")
    print("4. 8x7")
    print("5. 8x8")

def getXY(x):
    if (x == 1):
        return (6, 5)
    if (x == 2):
        return (6, 6)
    if (x == 3):
        return (7, 6)
    if (x == 4):
        return (8, 7)
    if (x == 5):
        return (8, 8)

def getSize():

    printInfo()

    while True:
        cmd = input(">>").split()

        try:
            if (len(cmd) == 1):
                try:
                    x = int(cmd[0])
                except:
                    raise raiseException("This in not an integer !")

                if (x > 0 and x < 6):
                    return getXY(x)
                else:
                    raise raiseException("This value is not between 1-5 !")
            else:
                raise raiseException("Invalid input!")
        except raiseException as ve:
            print (ve)


