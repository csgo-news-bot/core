import unittest

from src.service.parser.CreateMatchDTOFromUrl import CreateMatchDTOFromUrl


class ResultParserTestCase(unittest.TestCase):
    def test_find(self):
        self.assertEqual('bo1', CreateMatchDTOFromUrl().get_type('2 Best of 1 1'))
        self.assertEqual('bo3', CreateMatchDTOFromUrl().get_type('2 Best of 3 1'))
        self.assertEqual('bo5', CreateMatchDTOFromUrl().get_type('2 Best of 5 1'))
        self.assertEqual('bo3', CreateMatchDTOFromUrl().get_type('2 Bestsfafsfa 1'))
