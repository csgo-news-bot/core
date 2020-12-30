from typing import Set

from bs4 import BeautifulSoup
from src.entity import MatchEntity
from src.entity.TeamEntity import TeamEntity
from src.service.ConfigService import ConfigService
from src.service.CountryAllowService import CountryAllowService
from src.service.HttpClientService import HttpClientService
from src.service.LatestMatchesService import LatestMatchesService
from src.service.TelegramNotifierService import TelegramNotifierService


class Parser:
    added_items: Set = {}
    list_output = []
    config = None
    latest_matches_service = None
    telegram_notifier_service = None
    country_allow_service = None
    http_client_service = None
    results = None

    def __init__(self):
        self.config = ConfigService()
        self.latest_matches_service = LatestMatchesService()
        self.telegram_notifier_service = TelegramNotifierService()
        self.country_allow_service = CountryAllowService()
        self.http_client_service = HttpClientService()

    def execute(self):
        text = self.http_client_service.get_html_page(self.config.get_hltv_result_endpoint())

        soup = BeautifulSoup(text, "html.parser")
        matches = soup.find_all('div', {'data-zonedgrouping-headline-classes': 'standard-headline'})

        if len(matches):
            matches2 = matches[0].find_all('div', {'class': 'results-sublist'})
            our_matches = matches2[0]
            self.results = our_matches.find_all('div', {'class': 'result-con'})
            self.added_items = self.latest_matches_service.get_all()

            # TODO: REMOVE IN FUTURE
            if not isinstance(self.added_items, list):
                self.added_items = list(self.added_items)
            # END: REMOVE IN FUTURE

            self.generate_dict()
            self.loop_result()
            self.latest_matches_service.save(self.added_items)

    def generate_dict(self):
        for item in self.results:
            href = item.find('a', {'class': 'a-reset'})['href']

            match_entity = MatchEntity()
            match_entity.set_id(self._get_id(href))
            match_entity.set_href(self.config.HLTV_SITE + href)
            match_entity.set_type(item.find('div', {'class': 'map-text'}).getText())
            match_entity.set_event(item.find('span', {'class': 'event-name'}).getText())
            match_entity.set_stars(self._get_stars(item))

            html_page = self.http_client_service.get_html_page(self.config.HLTV_SITE + href)
            soup = BeautifulSoup(html_page, "html.parser")

            try:
                teams = soup.find('div', {"class": "standard-box teamsBox"}).find_all("div", {"class": "team"})
            except Exception:
                continue

            for team in teams:
                team_entity = TeamEntity()
                team_entity.set_score(team.find("div", {"class": ["won", "lost"]}).text)
                team_entity.set_title(team.find("img", {"class": "logo"})['title'])
                team_entity.set_country(team.find("img", {"class": ["team1", "team2"]})['title'])

                if team.find("div", {"class": "won"}):
                    match_entity.set_winner(team_entity)
                elif team.find("div", {"class": "lost"}):
                    match_entity.set_looser(team_entity)

            self.list_output.append(match_entity)

    def loop_result(self):
        for item in self.list_output:
            if item.get_id() in self.added_items:
                continue

            if self.country_allow_service.is_allow_country(item):
                self.telegram_notifier_service.notify(self.get_message(item))
                self.added_items.append(item.get_id())

    def get_message(self, item: MatchEntity):
        looser_hashtag = ''

        if item.get_winner().get_country() != item.get_looser().get_country():
            looser_hashtag = self._get_hashtag(item.get_looser().get_country())

        msg = f"""
{item.get_stars()}<b>{item.get_winner().get_title()}</b> выйграла у {item.get_looser().get_title()} 
со счетом <b>{item.get_winner().get_score()}</b> - {item.get_looser().get_score()} ({item.get_type()}) 
на турнире {item.get_event()}, подробнее <a href='{item.get_href()}'>здесь</a> \n\n
{self._get_hashtag(item.get_winner().get_title())} 
{self._get_hashtag(item.get_looser().get_title())} 
{self._get_hashtag(item.get_type())} 
{self._get_hashtag(item.get_winner().get_country())} 
{looser_hashtag}
            """

        return msg

    @staticmethod
    def _get_stars(item) -> str:
        data = item.find_all('i', {'class': 'fa-star'})
        if len(data):
            return "★" * len(data) + " "
        return ""

    @staticmethod
    def _get_hashtag(string: str) -> str:
        string = string.lower()
        string = string.replace(' ', '_').replace('-', '_')
        return f"%23{string}"

    @staticmethod
    def _get_id(string):
        data = string.split("/")[2]
        return int(data)
