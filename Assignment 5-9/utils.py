from validation.validator import validatorException


class tools:

    @staticmethod
    def getDistanceInDays(date1, date2):

        t1 = date1.split('/')
        t1 = int(t1[0]) + int(t1[1])*30 + int(t1[2])*365

        t2 = date2.split('/')
        t2 = int(t2[0]) + int(t2[1])*30 + int(t2[2])*365
        return t2 - t1

    @staticmethod
    def isInt(x):
        try:
            intId = int(x)

            if intId < 0:
                raise validatorException("Id must be positive !!!")
        except:
            raise validatorException("Id is not integer !!!")


    @staticmethod
    def mySort(list, function):
        pass