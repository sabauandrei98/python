from unittest import TestCase
from controler.controler import controler
from repository.repo import repository

class TestControler(TestCase):

    def setUp(self):
        self.__repo = repository(5, 5)
        self.__controler = controler(self.__repo)

    def test_getMap(self):
        self.__repo.markOnMap(0, 0, "X", "=")
        self.assertEqual(self.__controler.getMap(),
                         [["X", "X", "=", "=", "="], ["X", "X", "=", "=", "="], ["=", "=", "=", "=", "="],
                          ["=", "=", "=", "=", "="], ["=", "=", "=", "=", "="]])



    def test_movePlayer(self):
        self.__controler.movePlayer(1, 1, "X", "=")
        self.assertEqual(self.__controler.getMap(),
                         [["X", "X", "X", "=", "="], ["X", "X", "X", "=", "="], ["X", "X", "X", "=", "="],
                          ["=", "=", "=", "=", "="], ["=", "=", "=", "=", "="]])

    def test_getEmptyPoints(self):
        self.__controler.movePlayer(1, 1, "X", "=")
        self.assertEqual(self.__controler.getEmptyPoints("="), 16)

    def test_isMapFull(self):
        self.__controler.movePlayer(1, 1, "X", "=")
        self.assertEqual(self.__controler.isMapFull(self.__controler.getMap()), False)

        self.__controler.movePlayer(1, 3, "X", "=")
        self.assertEqual(self.__controler.isMapFull(self.__controler.getMap()), False)

        self.__controler.movePlayer(3, 1, "X", "=")
        self.assertEqual(self.__controler.isMapFull(self.__controler.getMap()), False)

        self.__controler.movePlayer(3, 3, "X", "=")
        self.assertEqual(self.__controler.isMapFull(self.__controler.getMap()), True)

    def test_moveAI(self):
        self.assertEqual(self.__controler.getEmptyPoints("="), 25)
        self.__controler.moveAI("O", "=")
        self.assertFalse(self.__controler.getEmptyPoints("=") == 25)
