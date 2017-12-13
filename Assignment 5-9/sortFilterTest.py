import unittest
import sortFilter

class testSort(unittest.TestCase):

    def setUp(self):
        self.__l = []
        self.__l.append((1, 3, 3))
        self.__l.append((2, 1, 4))
        self.__l.append((4, 6, 6))
        self.__l.append((8, 1, 3))
        self.__compareFunction = sortFilter.sortFunction
        self.__selectionSort = sortFilter.selectionSort


    def test_selectionSort(self):
        self.__selectionSort(self.__l, self.__compareFunction)
        self.assertTrue(self.__l == [(1, 3, 3), (2, 1, 4), (4, 6, 6), (8, 1, 3)])

        self.__selectionSort(self.__l, self.__compareFunction, 1)
        self.assertTrue(self.__l == [(2, 1, 4), (8, 1, 3), (1, 3, 3), (4, 6, 6)])

        self.__selectionSort(self.__l, self.__compareFunction, 2)
        self.assertTrue(self.__l == [(8, 1, 3), (1, 3, 3), (2, 1, 4), (4, 6, 6)])


class testFilter(unittest.TestCase):

    def setUp(self):
        self.__l = []
        self.__l.append((1, 3, 3))
        self.__l.append((2, 1, 4))
        self.__l.append((4, 6, 6))
        self.__l.append((8, 1, 3))
        self.__filter = sortFilter.filterList


    def test_filter(self):
        self.assertTrue(self.__filter(self.__l, lambda x: x[0] < 4) == [(1, 3, 3), (2, 1, 4)])
        self.assertTrue(self.__filter(self.__l, lambda x: x[1] == 6) == [(4, 6, 6)])