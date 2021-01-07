from bs4 import BeautifulSoup

from src.abstract.LoggerAbstract import LoggerAbstract
from src.service.ConfigService import ConfigService
from src.service.HttpClientService import HttpClientService


class ParseMatchesHTML(LoggerAbstract):
    http_client_service: HttpClientService = None
    config: ConfigService = None

    def __init__(self):
        super().__init__()
        self.http_client_service = HttpClientService()
        self.config = ConfigService()

    def get_matches(self, all_in_page=False) -> list:
        text = self.http_client_service.get_html_page(self.config.get_hltv_result_endpoint())
        self.logger.info(f'Opened {self.config.get_hltv_result_endpoint()}')

        soup = BeautifulSoup(text, "html.parser")
        matches = soup.find_all('div', {'data-zonedgrouping-headline-classes': 'standard-headline'})

        if len(matches):
            result = []
            if all_in_page:
                matches_list = matches[0].find_all('div', {'class': 'results-sublist'})
                for i in range(0, len(matches_list)-1):
                    result = result + matches_list[i].find_all('div', {'class': 'result-con'})
                return result
            else:
                matches_list = matches[0].find_all('div', {'class': 'results-sublist'})
                return matches_list[0].find_all('div', {'class': 'result-con'})
        return []
