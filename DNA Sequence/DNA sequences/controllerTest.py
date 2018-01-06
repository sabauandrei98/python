from unittest import TestCase

from controller.controller import controller
from domain.domain import DNA
from raiseEx import raiseException
from repo.repository import repository


class TestController(TestCase):
    def setUp(self):
        self.__repo = repository()
        self.__controller = controller(self.__repo)

    def test_add(self):
        self.__controller.addDna("TGA")
        self.assertEqual(len(self.__repo), 1)

        with self.assertRaises(raiseException):
            self.__repo.addItem(DNA("TGA"))

    def test_filter(self):
        self.__repo.addItem(DNA("TAG"))
        self.__repo.addItem(DNA("TGGGA"))
        self.__repo.addItem(DNA("TGTAG"))
        self.__repo.filter(DNA("TAG"))
        self.assertEqual(len(self.__repo), 2)

    def test_sortLongestRep(self):
        self.__repo.addItem(DNA("TAAAG"))
        self.__repo.addItem(DNA("TGGGGA"))
        self.__repo.addItem(DNA("TGTTTTTTAG"))

        l = sorted(self.__repo.getItems(), key=lambda x: -x.getLongestRep())
        self.assertEqual(l[0].getDna(), "TGTTTTTTAG")
