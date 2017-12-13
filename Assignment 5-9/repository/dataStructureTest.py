import unittest
from repository.dataStructure import dataStructure, item


class Test(unittest.TestCase):

    def setUp(self):
        self._items = dataStructure()

    def runTest(self):
        self.assertEqual(len(self._items), 0)
        self._items[1] = item(1, "and")
        self.assertEqual(self._items[1].data, "and")

        self._items[1] = item(1, "rei")
        self.assertEqual(self._items[1].data, "rei")
        del self._items[1]

        self.assertEqual(len(self._items), 0)
        self._items[1] = item(1, "a")
        self._items[2] = item(2, "b")
        self._items[3] = item(3, "c")
        self._items[4] = item(4, "d")

        for x in self._items:
            print(x)

        del self._items[1]
        del self._items[2]
        del self._items[3]
        del self._items[4]
        self.assertEqual(len(self._items), 0)