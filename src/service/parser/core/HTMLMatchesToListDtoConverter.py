from src.helpers.string import StringHelper
from src.service.parser.CreateMatchDTOFromUrl import CreateMatchDTOFromUrl


class HTMLMatchesToListDtoConverter:
    create_match_dto_from_url: CreateMatchDTOFromUrl

    def __init__(self):
        super().__init__()
        self.create_match_dto_from_url = CreateMatchDTOFromUrl()

    def get_list_of_dto(self, html_matches: list, hltv_ids_added_today: list) -> list:
        result = []
        list_ids = [item.hltv_id for item in hltv_ids_added_today]

        if len(html_matches) == 0:
            return []

        for item in html_matches:
            href = item.find('a', {'class': 'a-reset'})['href']

            if StringHelper.search_list_id_in_string(list_ids=list_ids, string=href):
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
