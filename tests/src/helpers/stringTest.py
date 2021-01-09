import unittest
from src.helpers.string import StringHelper


class StringHelperTestCase(unittest.TestCase):
    def test_url_parse(self):
        self.assertEqual('.png', StringHelper.get_extension_from_url('https://www.hltv.org/img/static/flags/300x200/FR.png'))
