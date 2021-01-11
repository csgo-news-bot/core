import unittest
from src.helpers.string import StringHelper


class StringHelperTestCase(unittest.TestCase):
    def test_url_parse(self):
        self.assertEqual('.png', StringHelper.get_extension_from_url('https://www.hltv.org/img/static/flags/300x200/FR.png'))

    def test_search_list_id_in_string(self):
        string = 'https://www.hltv.org/matches/2346047/sprout-vs-ssp-united-pro-series-winter-2020'
        self.assertFalse(StringHelper.search_list_id_in_string(list_ids=[123321, 1233211], string=string))
        self.assertFalse(StringHelper.search_list_id_in_string(list_ids=[], string=string))
        self.assertTrue(StringHelper.search_list_id_in_string(list_ids=[123321, 1233211, 2346047], string=string))
