import unittest

from src.service.creator.MatchCreator import MatchCreator


class MatchCreatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.classname = MatchCreator()

    def test_types(self):
        self.assertEqual(1, 2)
