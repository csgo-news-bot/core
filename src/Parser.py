from typing import Set

import requests
import sys
from bs4 import BeautifulSoup
from src.entity.MatchEntity import MatchEntity
from src.entity.TeamEntity import TeamEntity
from src.service.ConfigService import ConfigService
from src.service.CountryAllowSerivce import CountryAllowService
from src.service.LatestMatchesService import LatestMatchesService
from src.service.TelegramNotifierService import TelegramNotifierService


class Parser():
    site = "https://www.hltv.org"
    url = site + "/results"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    r = ''
    text = ''
    added_items: Set = {}
    list_output = []
    config = None

    def __init__(self):
        self.config = ConfigService()
        self.latestMatchesService = LatestMatchesService()
        self.telegramNotifierService = TelegramNotifierService()
        self.countryAllowService = CountryAllowService()

    def execute(self):
        self.r = requests.get(self.url, headers=self.headers)
        self.text = self.r.text
        self.main()

    def main(self):
        soup = BeautifulSoup(self.text, "html.parser")
        matches = soup.find_all('div', {'data-zonedgrouping-headline-classes': 'standard-headline'})
        if len(matches):
            matches2 = matches[0].find_all('div', {'class': 'results-sublist'})
            our_matches = matches2[0]
            self.results = our_matches.find_all('div', {'class': 'result-con'})
            self.added_items = self.latestMatchesService.getAll()
            self.generate_dict()
            self.loop_result()
            self.latestMatchesService.save(self.added_items)

    def get_stars(self, item):
        data = item.find_all('i', {'class': 'fa-star'})
        if len(data):
            return "★" * len(data) + " "
        return ""

    def get_hashtag(self, str):
        str = str.lower()
        str = str.replace(' ', '_').replace('-', '_')
        return f"%23{str}"

    def get_id(self, string):
        data = string.split("/")[2]
        return int(data)

    def generate_dict(self):
        for item in self.results:
            href = item.find('a', {'class': 'a-reset'})['href']

            matchEntity = MatchEntity()
            matchEntity.setId(self.get_id(href))
            matchEntity.setHref(self.site + href)
            matchEntity.setType(item.find('div', {'class': 'map-text'}).getText())
            matchEntity.setEvent(item.find('span', {'class': 'event-name'}).getText())
            matchEntity.setStars(self.get_stars(item))

            r = requests.get(self.site + href, headers=self.headers)

            soup = BeautifulSoup(r.text, "html.parser")

            try:
                teams = soup.find('div', {"class": "standard-box teamsBox"}).find_all("div", {"class": "team"})
            except Exception as e:
                continue

            for team in teams:
                teamEntity = TeamEntity()
                teamEntity.setScore(team.find("div", {"class": ["won", "lost"]}).text)
                teamEntity.setTitle(team.find("img", {"class": "logo"})['title'])
                teamEntity.setCountry(team.find("img", {"class": ["team1", "team2"]})['title'])

                if team.find("div", {"class": "won"}):
                    matchEntity.setWinner(teamEntity)
                elif team.find("div", {"class": "lost"}):
                    matchEntity.setLooser(teamEntity)

            self.list_output.append(matchEntity)

    def loop_result(self):
        for item in self.list_output:
            if item.getId() in self.added_items: continue

            if self.countryAllowService.isAllowCountry(item):
                self.telegramNotifierService.notify(self.get_message(item))
                self.added_items.add(item.getId())

    def get_message(self, item: MatchEntity):
        looser_hashtag = ''

        if item.getWinner().getCountry() == item.getLooser().getCountry():
            looser_hashtag = self.get_hashtag(item.getLooser().getCountry())

        msg = f"""
{item.getStars()}<b>{item.getWinner().getTitle()}</b> выйграла у {item.getLooser().getTitle()} 
со счетом <b>{item.getWinner().getScore()}</b> - {item.getLooser().getScore()} ({item.getType()}) 
на турнире {item.getEvent()}, подробнее <a href='{item.getHref()}'>здесь</a> \n\n
{self.get_hashtag(item.getWinner().getTitle())} 
{self.get_hashtag(item.getLooser().getTitle())} 
{self.get_hashtag(item.getType())} 
{self.get_hashtag(item.getWinner().getCountry())} 
{looser_hashtag}
            """
        print(msg)
        return msg
