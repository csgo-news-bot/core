from src.repository.MatchRepository import MatchRepository
from src.service.parser.core.ParseMatchesHTML import ParseMatchesHTML


class HLTVParser:
    parse_matches_html: ParseMatchesHTML = None

    def __init__(self):
        self.parse_matches_html = ParseMatchesHTML()
        self.match_repository = MatchRepository()

    def execute(self):
        current_parsed_matches_list = self.parse_matches_html.get_matches()
        latest_added_to_db_matches = self.match_repository.get_all_by_datetime()
