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

    def get_matches(self, page: int = None) -> list:
        result = []

        link = self._get_link(page)
        text = self.http_client_service.get_html_page(link)
        self.logger.info(f'Opened {link}')

        soup = BeautifulSoup(text, "html.parser")

        if page is None:
            matches = soup.find_all('div', {'data-zonedgrouping-headline-classes': 'standard-headline'})
            matches_list = matches[0].find_all('div', {'class': 'results-sublist'})
            for i in range(0, len(matches_list) - 1):
                result = result + matches_list[i].find_all('div', {'class': 'result-con'})
            return result

        if page:
            return soup.find_all('div', {'class': 'result-con', 'data-zonedgrouping-entry-unix': True})

    def _get_link(self, page: int = None) -> str:
        offset = ''
        if page > 1:
            offset = f'?offset={(page - 1) * 100}'
        return f'{self.config.get_hltv_result_endpoint()}{offset}'
