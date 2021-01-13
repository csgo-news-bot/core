from typing import Set

from src.models import MatchModel


class CountryAllowService:
    countries: Set = {
        'Ukraine',
        'Belarus',
        'Kazakhstan',
        'Russia'
    }

    def is_allow_country(self, match: MatchModel) -> bool:
        return bool(
            {match.team_won.country.title, match.team_lose.country.title}.intersection(self.countries)
        )
