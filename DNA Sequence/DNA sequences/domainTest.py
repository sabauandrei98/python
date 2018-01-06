from unittest import TestCase
from domain.domain import DNA


class TestRepository(TestCase):
    def setUp(self):
        pass

    def test_domain(self):
        dna = DNA("TAGGG")
        self.assertEqual(dna.getDna(), "TAGGG")
        dna.setDna("TAG")
        self.assertEqual(dna.getDna(), "TAG")
        self.assertEqual(len(dna), 3)
