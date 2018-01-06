from exceptions import raiseException

class validator:

    @staticmethod
    def isInt(n):
        try:
            x = int(n)
            return True
        except:
            raise raiseException("Coords are not numbers !")

    @staticmethod
    def pointOnMap(x, y):
        maxSize = 8 - 1
        x = int(x)
        y = int(y)

        if x > maxSize or y > maxSize or x < 0 or y < 0:
            return False

        return True

    @staticmethod
    def checkInput(cmd):

        if len(cmd) != 2:
            raise raiseException("Invalid input length !")

        if validator.isInt(cmd[0]) and validator.isInt(cmd[1]):
            pass

        if not validator.pointOnMap(cmd[0], cmd[1]):
            raise raiseException("No such point on map !")

