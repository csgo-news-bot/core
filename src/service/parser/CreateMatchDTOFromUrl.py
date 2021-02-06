import time

from bs4 import BeautifulSoup

from src.abstract.LoggerAbstract import LoggerAbstract
from src.dto.MatchDTO import MatchDTO
from src.dto.TeamDTO import TeamDTO
from src.helpers.time import DateTimeHelper
from src.service.ConfigService import ConfigService
from src.service.HttpClientService import HttpClientService


class CreateMatchDTOFromUrl(LoggerAbstract):
    config: ConfigService = None

    def __init__(self):
        super().__init__()
        self.config = ConfigService()
        self.http_client_service = HttpClientService()

    def create(self, href: str):
        html_page = self.http_client_service.get_html_page(self.config.HLTV_SITE + href)

        self.logger.info(f'Opened {self.config.HLTV_SITE + href}')

        soup = BeautifulSoup(html_page, "html.parser")

        try:
            teams = soup.find('div', {"class": "standard-box teamsBox"}).find_all("div", {"class": "team"})
        except Exception as e:
            self.logger.error(e, exc_info=True)
            return None

        match_dto = self.__create_match_dto(item=soup.find('div', {"class": "match-page"}), href=href)

        for team in teams:
            team_dto = self.__create_team_dto(team)

            if team.find("div", {"class": "won"}):
                match_dto.winner = team_dto
            elif team.find("div", {"class": "lost"}):
                match_dto.looser = team_dto

        time.sleep(1)

        return match_dto

    def __create_team_dto(self, team) -> TeamDTO:
        team_dto = TeamDTO()
        team_dto.score = team.find("div", {"class": ["won", "lost"]}).text
        team_dto.title = team.find("img", {"class": "logo"})['title']
        team_dto.country = team.find("img", {"class": ["team1", "team2"]})['title']
        team_dto.country_image_url = team.find("img", {"class": ["team1", "team2"]})['src']
        team_dto.set_image_url(team.find("img", {"class": "logo"})['src'])

        return team_dto

    def __create_match_dto(self, item, href: str) -> MatchDTO:
        match_dto = MatchDTO()
        match_dto.id = self._get_id(href)
        match_dto.href = self.config.HLTV_SITE + href
        match_dto.type = self.get_type(item.find('div', {'class': 'veto-box'}).getText())
        match_dto.event = item\
            .find('div', {'class': 'timeAndEvent'})\
            .find('div', {'class': 'text-ellipsis'})\
            .find('a').getText()
        unix_time = item.find('div', {'class': 'timeAndEvent'}).find('div', {'class': 'date'})['data-unix']
        match_dto.played_at = DateTimeHelper.unix_time_to_datetime(int(unix_time))
        return match_dto

    @staticmethod
    def _get_id(string: str) -> int:
        data = string.split("/")[2]
        return int(data)

    @staticmethod
    def get_type(string: str) -> str:
        type_map = {
            'Best of 1': 'bo1',
            'Best of 3': 'bo3',
            'Best of 5': 'bo5',
        }
        for k, v in type_map.items():
            if string.find(k) != -1:
                return v

        return 'bo3'
