from src.service.creator.FullMatchCreator import FullMatchCreator
from src.service.parser.core.HTMLMatchesToListDtoConverter import HTMLMatchesToListDtoConverter
from src.service.parser.core.ParseMatchesHTML import ParseMatchesHTML


class HLTVParser:
    parse_matches_html: ParseMatchesHTML
    html_matches_converter: HTMLMatchesToListDtoConverter
    full_match_creator: FullMatchCreator

    def __init__(self):
        self.parse_matches_html = ParseMatchesHTML()
        self.html_matches_converter = HTMLMatchesToListDtoConverter()
        self.full_match_creator = FullMatchCreator()

    def execute(self, page: int = None, default_published_match: bool = None):
        """
        :param page: Parse all matches on page.
                      -  None is latest matches
                      -  1 is all matches on first page
        :param default_published_match: Set default value `published_match` to every match
        :return:
        """
        matches = self.parse_matches_html.get_matches(page=page)
        dto_list = self.html_matches_converter.get_list_of_dto(
            html_matches=matches,
        )

        if len(dto_list) > 0:
            self.full_match_creator.process_to_create(
                list_of_dtos=dto_list,
                default_published_match=default_published_match
            )
