from unittest import TestCase

from domain.book import book
from domain.client import client
from domain.rental import rental
from validation.validator import *
from exceptions.exceptions import *

class testValidation(TestCase):
    def setUp(self):
        self.__bookValidator = bookValidator()
        self.__clientValidator = clientValidator()
        self.__rentalValidator = rentalValidator()

    def test_bookValidation(self):
        b = book(1, "Title", "Desc", "Author")
        self.assertTrue(self.__bookValidator.validate(b) == True)

        c = book(-1, "Title", "Desc", "Author")
        try:
            self.__bookValidator.validate(c)
        except:
            pass

        c = book("d", "Title", "Desc", "Author")
        try:
            self.__bookValidator.validate(c)
        except:
            pass


    def test_clientValidation(self):
        b = client(1, "Andrei")
        self.assertTrue(self.__clientValidator.validate(b) == True)

        c = client(-5, "Andrei")
        try:
            self.__clientValidator.validate(c)
        except:
            pass

        c = client("dasd", "Andrei")
        try:
            self.__clientValidator.validate(c)
        except:
            pass


    def test_rentalValidation(self):
        b = rental(1, 1, 1, "11/11/2017", "12/12/2017", "-")
        self.assertTrue(self.__rentalValidator.validate(b) == True)

        b = rental(1, 1, 1, "11/dd/2017", "12/12/2017", "-")
        try:
            self.__rentalValidator.validate(b)
        except:
            pass

        b = rental(-1, 1, 1, "11/dd/2017", "12/12/2017", "-")
        try:
            self.__rentalValidator.validate(b)
        except:
            pass

        b = rental("dasd", 1, 1, "11/dd/2017", "12/12/2017", "-")
        try:
            self.__rentalValidator.validate(b)
        except:
            pass

        b = rental(1, 1, 1, "11/dd/2017/123", "12/12/2017", "-")
        try:
            self.__rentalValidator.validate(b)
        except:
            pass

        b = rental(1, 1, 1, "13/01/2019", "12/12/2018", "-")
        try:
            self.__rentalValidator.validate(b)
        except:
            pass

        b = rental(1, 1, 1, "13/12/2018", "12/12/2018", "-")
        try:
            self.__rentalValidator.validate(b)
        except:
            pass