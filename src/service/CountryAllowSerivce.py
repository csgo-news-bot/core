from typing import Set

from src import MatchEntity


class CountryAllowService:
    countries: Set = {
        'Ukraine',
        'Belarus',
        'Kazakhstan',
        'Russia'
    }

    def is_allow_country(self, match: MatchEntity) -> bool:
        return bool(
            {match.get_winner().get_country(), match.get_looser().get_country()}.intersection(self.countries)
        )
