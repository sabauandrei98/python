from unittest import TestCase

from domain.book import book


class testBook(TestCase):
    def setUp(self):
        self.__book = book(1, "Title", "Desc", "Author")

    def tearDown(self):
        self.__book = None

    def test_getData(self):
        self.assertTrue(self.__book.getId() == 1)
        self.assertTrue(self.__book.getTitle() == "Title")
        self.assertTrue(self.__book.getDescription() == "Desc")
        self.assertTrue(self.__book.getAuthor() == "Author")

    def test_setData(self):
        self.__book.setId(2)
        self.assertTrue(self.__book.getId() == 2)

        self.__book.setTitle("Title1")
        self.assertTrue(self.__book.getTitle() == "Title1")

        self.__book.setDescription("Desc1")
        self.assertTrue(self.__book.getDescription() == "Desc1")

        self.__book.setAuthor("Author1")
        self.assertTrue(self.__book.getAuthor() == "Author1")

    def test_string(self):
        print(self.__book + "String")



