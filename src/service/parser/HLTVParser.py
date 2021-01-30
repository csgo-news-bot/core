import datetime

from src.repository.MatchRepository import MatchRepository
from src.service.creator.FullMatchCreator import FullMatchCreator
from src.service.parser.core.HTMLMatchesToListDtoConverter import HTMLMatchesToListDtoConverter
from src.service.parser.core.ParseMatchesHTML import ParseMatchesHTML


class HLTVParser:
    parse_matches_html: ParseMatchesHTML
    match_repository: MatchRepository
    html_matches_converter: HTMLMatchesToListDtoConverter
    full_match_creator: FullMatchCreator

    def __init__(self):
        self.parse_matches_html = ParseMatchesHTML()
        self.match_repository = MatchRepository()
        self.html_matches_converter = HTMLMatchesToListDtoConverter()
        self.full_match_creator = FullMatchCreator()

    def execute(self, **kwargs):
        dto_list = self.html_matches_converter.get_list_of_dto(
            html_matches=self.parse_matches_html.get_matches(kwargs),
        )

        if len(dto_list) == 0:
            return None

        self.full_match_creator.process_to_create(
            list_of_dtos=dto_list
        )
