import time
from bs4 import BeautifulSoup

from src.abstract.LoggerAbstract import LoggerAbstract
from src.dto.MatchDTO import MatchDTO
from src.dto.TeamDTO import TeamDTO
from src.helpers.time import DateTimeHelper
from src.service.ConfigService import ConfigService
from src.service.HttpClientService import HttpClientService


class HTMLMatchesToListDtoConverter(LoggerAbstract):
    config: ConfigService

    def __init__(self):
        super().__init__()
        self.config = ConfigService()
        self.http_client_service = HttpClientService()

    def get_list_of_dto(self, html_matches: list) -> list:
        result = []

        if len(html_matches) == 0:
            return []

        for item in html_matches:
            href = item.find('a', {'class': 'a-reset'})['href']

            match_dto = MatchDTO()
            match_dto.id = self._get_id(href)
            match_dto.href = self.config.HLTV_SITE + href
            match_dto.type = item.find('div', {'class': 'map-text'}).getText()
            match_dto.event = item.find('span', {'class': 'event-name'}).getText()
            match_dto.stars = self._get_count_stars(item)
            match_dto.played_at = DateTimeHelper.unix_time_to_datetime(int(item['data-zonedgrouping-entry-unix']))

            html_page = self.http_client_service.get_html_page(self.config.HLTV_SITE + href)
            self.logger.info(f'Opened {self.config.HLTV_SITE + href}')
            soup = BeautifulSoup(html_page, "html.parser")
            time.sleep(1)

            try:
                teams = soup.find('div', {"class": "standard-box teamsBox"}).find_all("div", {"class": "team"})
            except Exception:
                continue

            for team in teams:
                team_dto = TeamDTO()
                team_dto.score = team.find("div", {"class": ["won", "lost"]}).text
                team_dto.title = team.find("img", {"class": "logo"})['title']
                team_dto.country = team.find("img", {"class": ["team1", "team2"]})['title']
                team_dto.country_image_url = team.find("img", {"class": ["team1", "team2"]})['src']
                team_dto.image_url = team.find("img", {"class": "logo"})['src']

                if team.find("div", {"class": "won"}):
                    match_dto.winner = team_dto
                elif team.find("div", {"class": "lost"}):
                    match_dto.looser = team_dto

            result.append(match_dto)

        return result

    @staticmethod
    def _get_count_stars(item) -> int:
        data = item.find_all('i', {'class': 'fa-star'})
        if len(data):
            return len(data)
        return 0

    @staticmethod
    def _get_id(string: str) -> int:
        data = string.split("/")[2]
        return int(data)
