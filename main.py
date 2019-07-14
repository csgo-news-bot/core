# coding: utf8
import requests
import json
import os
import datetime
from bs4 import BeautifulSoup

from dotenv import load_dotenv
load_dotenv()

PATH = os.path.dirname(os.path.abspath(__file__))

class Parser():
    site = "https://www.hltv.org"
    url = site + "/results"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }
    r = ''
    text = ''
    file_name = os.path.join(PATH, 'events_items.json')
    added_items = []
    list_output = []

    countries_list = [
        'Ukraine',
        'Belorussia',
        'Kazakhstan',
        'Russia'
    ]

    def __init__(self):
        self.r = requests.get(self.url, headers=self.headers)
        self.text = self.r.text
        self.main()


    def getFileName(self):
        now = datetime.datetime.now()
        return f"{now.year}-{now.month}-{now.day}"

    def main(self):
        soup = BeautifulSoup(self.text, "html.parser")
        matches = soup.find_all('div', {'data-zonedgrouping-headline-classes': 'standard-headline'})
        if len(matches):
            matches2 = matches[0].find_all('div', {'class': 'results-sublist'})
            our_matches = matches2[0]
            self.results = our_matches.find_all('div', {'class': 'result-con'})
            self.added_items = self.read_json()
            self.generate_dict()
            self.loop_result()
            self.save_json()

    def read_json(self):
        with open(self.file_name) as f:
            data = json.load(f)
        return data['items']

    def save_json(self):
        data = {
            'items': self.added_items[-100:]
        }
        with open(self.file_name, 'w') as outfile:
            outfile.write(json.dumps(data))

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

            one_match = {
                'id': self.get_id(href),
                'teams': {
                    'winner': {},
                    'looser': {}
                },
                'href': self.site + href,
                'type': item.find('div', {'class': 'map-text'}).getText(),
                'event': item.find('span', {'class': 'event-name'}).getText(),
                'stars': self.get_stars(item)

            }


            r = requests.get(self.site + href, headers=self.headers)
            text = r.text
            soup = BeautifulSoup(text, "html.parser")

            teams = soup.find('div', {"class": "standard-box teamsBox"}).find_all("div", {"class": "team"})

            for team in teams:
                current_item = {
                    'score': team.find("div", {"class":["won","lost"]}).text,
                    'title': team.find("img",{"class":"logo"})['title'],
                    'country': team.find("img", {"class": ["team1", "team2"]})['title'],
                }
                if team.find("div", {"class": "won"}):
                    one_match['teams']['winner'] = current_item
                else:
                    one_match['teams']['looser'] = current_item
            self.list_output.append(one_match)

    def telegram_bot_sendtext(self, bot_message):
        # 188118870
        bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        bot_chatID = os.getenv("TELEGRAM_CHAT_ID")
        # bot_chatID = '188118870'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text=' + bot_message
        requests.get(send_text)

    def handler(self, item):
        msg = self.get_message(item)
        self.telegram_bot_sendtext(msg)

    def loop_result(self):
        for item in self.list_output:
            if item['id'] in self.added_items: continue
            if self.filters(item['teams']['winner']['country']) or self.filters(item['teams']['looser']['country']):
                self.handler(item)
                self.added_items.append(item['id'])

    def get_message(self, item):
        looser_hashtag = '' if item['teams']['winner']['country'] == item['teams']['winner']['country']  \
        else self.get_hashtag(['teams']['looser']['country'])

        msg = f"{item['stars']}<b>{item['teams']['winner']['title']}</b> выйграла у {item['teams']['looser']['title']} "
        msg = msg + f"со счетом <b>{item['teams']['winner']['score']}</b> - {item['teams']['looser']['score']} ({item['type']}) "
        msg = msg + f"на турнире {item['event']}, подробнее <a href='{item['href']}'>здесь</a> \n\n"
        msg = msg + f"{self.get_hashtag(item['teams']['winner']['title'])} " \
            f"{self.get_hashtag(item['teams']['looser']['title'])} " \
            f"{self.get_hashtag(item['type'])} "\
            f"{self.get_hashtag(item['teams']['winner']['country'])} "\
            f"{looser_hashtag}"\

        return msg

    def filters(self, country):
        if country in self.countries_list:
            return True
        return False

Parser()
