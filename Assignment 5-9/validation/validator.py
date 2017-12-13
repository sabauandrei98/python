from exceptions.exceptions import raiseException


class validatorException(raiseException):
    pass


class bookValidator:

    def validateId(self, id):
        try:
            intId = int(id)

            if intId < 0:
                raise validatorException("Id must be positive !!!")
        except:
            raise validatorException("Id is not integer !!!")

    def validate(self, b):
        self.validateId(b.getId())
        return True



class clientValidator:

    def validateId(self, id):
        try:
            intId = int(id)

            if intId < 0:
                raise validatorException("Id must be positive !!!")
        except:
            raise validatorException("Id is not integer !!!")

    def validate(self, client):
        self.validateId(client.getId())
        return True


class rentalValidator:

    def validateId(self, id):
        try:
            intId = int(id)

            if intId < 0:
                raise validatorException("Id must be positive !!!")
        except:
            raise validatorException("Id is not integer !!!")

    def validateDate(self, date):
        try:
            date = date.split('/')
            if(len(date) != 3):
                raise validatorException("Invalid date format")
            else:
                if int(date[0]) < 0 or int(date[0]) > 31 or int(date[1]) < 0 or int(date[1]) > 12 or int(date[2]) < 2017:
                    raise validatorException("Invalid date format")
        except:
            raise validatorException("Invalid date format")


    def dateInPast(self, date1, date2):

        date1 = date1.split('/')
        date2 = date2.split('/')

        t1 = int(date1[0]) + int(date1[1]) * 30
        t2 = int(date2[0]) + int(date2[1]) * 30

        if (int(date1[2]) > int(date2[2])):
            raise validatorException("Invalid dueDate must be in future !")

        if int(date1[2]) == int(date2[2]) and t1 > t2:
            raise validatorException("Invalid dueDate must be in future !")



    def validate(self, rental):
        self.validateId(rental.getId())
        self.validateId(rental.getBookId())
        self.validateId(rental.getClientId())
        self.validateDate(rental.getRentedDate())
        self.validateDate(rental.getDueDate())
        self.dateInPast(rental.getRentedDate(), rental.getDueDate())
        return True


