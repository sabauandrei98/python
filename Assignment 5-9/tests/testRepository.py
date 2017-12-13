from unittest import TestCase

from repository.repository import *
from domain.book import book
from exceptions.exceptions import raiseException

class TestRepository(TestCase):
    def setUp(self):
        self.__repo = repository()

    def test_addItem(self):
        b = book(1, "Title", "Desc", "Author")
        self.__repo.addItem(b)
        self.assertRaises(raiseException, self.__repo.addItem, b)

    def test_removeItem(self):
        b = book(1, "Title", "Desc", "Author")
        self.__repo.addItem(b)
        self.__repo.removeItem(1)
        self.assertTrue(len(self.__repo) == 0)

    def test_updateItem(self):
        b = book(1, "Title", "Desc", "Author")
        c = book(1, "Title2", "Desc2", "Author2")
        self.__repo.addItem(b)
        self.__repo.updateItem(c)
        self.assertTrue(len(self.__repo) == 1)

    def test_getItems(self):
        b = book(1, "Title", "Desc", "Author")
        c = book(2, "Title2", "Desc2", "Author2")
        self.__repo.addItem(b)
        self.__repo.addItem(c)
        l = self.__repo.getItems()
        self.assertTrue(len(self.__repo) == 2)
        self.assertTrue(l[0] == b)
        self.assertTrue(l[1] == c)

