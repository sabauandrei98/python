from unittest import TestCase
from repository.repo import repository

class TestRepository(TestCase):

    def setUp(self):
        self.__repo = repository(5,5)

    def test_getXY(self):
        self.assertEqual(self.__repo.getXY(), (5,5))

    def test_markOnMap(self):
        self.__repo.markOnMap(0, 0, "X", "=")
        self.assertEqual(self.__repo.getEmptyPoints("="), 21)

    def test_getPointSymbol(self):
        self.__repo.markOnMap(0, 0, "X", "=")
        self.assertEqual(self.__repo.getPointSymbol(1,1), "X")

    def test_getMap(self):
        self.__repo.markOnMap(0, 0, "X", "=")
        self.assertEqual(self.__repo.getMap(), [["X","X","=","=","="], ["X","X","=","=","="],["=","=","=","=","="],["=","=","=","=","="],["=","=","=","=","="]])

    def test_getEmptyPoints(self):
        self.__repo.markOnMap(1, 1, "X", "=")
        self.assertEqual(self.__repo.getEmptyPoints("="), 16)
