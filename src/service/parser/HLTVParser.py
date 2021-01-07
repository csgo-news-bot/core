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

    def execute(self):
        dto_list = self.html_matches_converter.get_list_of_dto(
            self.parse_matches_html.get_matches()
        )

        list_parsed_hltv_ids = [dto.id for dto in dto_list]

        black_list = []
        if len(list_parsed_hltv_ids) != 0:
            items = self.match_repository.get_all_by_hltv_list_ids(
                list_ids=list_parsed_hltv_ids
            )
            black_list = [dto.hltv_id for dto in items]

        self.full_match_creator.process_to_create(
            list_of_dtos=dto_list,
            black_list=black_list
        )
