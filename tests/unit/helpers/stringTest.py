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

    def test_get_hashtag(self):
        self.assertEqual("#team_x", StringHelper.get_hashtag("team-x"))
        self.assertEqual("#team_x", StringHelper.get_hashtag("team x"))

    def test_get_match_id_from_url(self):
        url = "https://www.hltv.org/matches/2346295/pain-vs-rebirth-dreamhack-open-january-2021-north-america"
        self.assertEqual(2346295, StringHelper.get_match_id_from_url(url))
