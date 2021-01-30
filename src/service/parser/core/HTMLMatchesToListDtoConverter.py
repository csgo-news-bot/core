from src.helpers.string import StringHelper
from src.repository.MatchRepository import MatchRepository
from src.service.parser.CreateMatchDTOFromUrl import CreateMatchDTOFromUrl


class HTMLMatchesToListDtoConverter:
    create_match_dto_from_url: CreateMatchDTOFromUrl
    match_repository: MatchRepository

    def __init__(self):
        super().__init__()
        self.create_match_dto_from_url = CreateMatchDTOFromUrl()
        self.match_repository = MatchRepository()


    def get_list_of_dto(self, html_matches: list) -> list:
        result = []

        if len(html_matches) == 0:
            return []

        for item in html_matches:
            href = item.find('a', {'class': 'a-reset'})['href']
            match_id = StringHelper.get_match_id_from_url(href)

            if self.match_repository.get_by_hltv_id(match_id):
                continue

            match_dto = self.create_match_dto_from_url.create(href=href)
            match_dto.stars = self._get_count_stars(item)
            match_dto.type = item.find('div', {'class': 'map-text'}).getText()

            if match_dto:
                result.append(match_dto)

        return result

    @staticmethod
    def _get_count_stars(item) -> int:
        data = item.find_all('i', {'class': 'fa-star'})
        if len(data):
            return len(data)
        return 0
