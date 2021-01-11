import unittest

from bs4 import BeautifulSoup

from src.dto.TeamDTO import TeamDTO
from src.service.HttpClientService import HttpClientService


class ResultParserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        http_client_service = HttpClientService()
        html_page = http_client_service.get_html_page(
            'https://www.hltv.org/matches/2346036/thedice-vs-game-fist-numberone-season-1'
        )
        self.soup = BeautifulSoup(html_page, "html.parser")

    def test_find(self):
        teams = self.soup.find('div', {"class": "standard-box teamsBox"}).find_all("div", {"class": "team"})
        for team in teams:
            team_dto = TeamDTO()
            team_dto.score = team.find("div", {"class": ["won", "lost"]}).text
            team_dto.title = team.find("img", {"class": "logo"})['title']
            team_dto.country = team.find("img", {"class": ["team1", "team2"]})['title']
            team_dto.country_image_url = team.find("img", {"class": ["team1", "team2"]})['src']
            team_dto.image_url = team.find("img", {"class": "logo"})['src']

            if team.find("div", {"class": "won"}):
                winner = team_dto
            elif team.find("div", {"class": "lost"}):
                looser = team_dto

        self.assertEqual(looser.country, 'Belgium')
        self.assertEqual(winner.country, 'France')
        self.assertEqual(looser.score, '5')
        self.assertEqual(winner.score, '16')
        self.assertEqual(looser.title, 'Game Fist')
        self.assertEqual(winner.title, 'TheDice')
        self.assertEqual(looser.country_image_url, '/img/static/flags/300x200/BE.png')
        self.assertEqual(winner.country_image_url, '/img/static/flags/300x200/FR.png')
        self.assertTrue(looser.image_url.startswith('https://img-cdn.hltv.org/teamlogo/'))
        self.assertTrue(winner.image_url.startswith('https://img-cdn.hltv.org/teamlogo/'))
