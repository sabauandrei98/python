from unittest import TestCase

from raiseEx import raiseException
from repo.repository import repository
from domain.domain import DNA

class TestRepository(TestCase):
    def setUp(self):
        self.__repo = repository()

    def test_addItem(self):
        dna = DNA("TAG")
        self.__repo.addItem(dna)
        self.assertEqual(len(self.__repo), 1)


        with self.assertRaises(raiseException):
            self.__repo.addItem(dna)

    def test_filter(self):
        self.__repo.addItem(DNA("TAG"))
        self.__repo.addItem(DNA("TGGGA"))
        self.__repo.addItem(DNA("TGTAG"))

        self.__repo.filter(DNA("TAG"))
        self.assertEqual(len(self.__repo), 2)



