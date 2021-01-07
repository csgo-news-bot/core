from bs4 import BeautifulSoup

from src.service.ConfigService import ConfigService
from src.service.HttpClientService import HttpClientService


class ParseMatchesHTML:
    http_client_service: HttpClientService = None
    config: ConfigService = None

    def __init__(self):
        self.http_client_service = HttpClientService()
        self.config = ConfigService()

    def get_matches(self) -> list:
        text = self.http_client_service.get_html_page(self.config.get_hltv_result_endpoint())

        soup = BeautifulSoup(text, "html.parser")
        matches = soup.find_all('div', {'data-zonedgrouping-headline-classes': 'standard-headline'})

        if len(matches):
            matches_list = matches[0].find_all('div', {'class': 'results-sublist'})
            return matches_list[0].find_all('div', {'class': 'result-con'})

        return []
