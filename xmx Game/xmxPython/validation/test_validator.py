from unittest import TestCase

from exceptions import raiseException
from validation.validation import validator

class TestValidator(TestCase):
    def test_isInt(self):
        self.assertEqual(validator.isInt(3), True)

        with self.assertRaises(raiseException):
            validator.isInt("r")


    def test_pointOnMap(self):
        self.assertEqual(validator.pointOnMap(1, 2, 5, 5), True)
        self.assertEqual(validator.pointOnMap(1, 8, 5, 5), False)

    def test_checkInput(self):

        with self.assertRaises(raiseException):
            validator.checkInput(["2", "3", "4"], 10, 11)

        with self.assertRaises(raiseException):
            validator.checkInput(["r", "3"], 10, 11)

        with self.assertRaises(raiseException):
            validator.checkInput(["12", "3"], 10, 11)
