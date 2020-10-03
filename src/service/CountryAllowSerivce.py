from typing import Set

from src.entity.MatchEntity import MatchEntity


class CountryAllowService:
    countries: Set = {
        'Ukraine',
        'Belorussia',
        'Kazakhstan',
        'Russia'
    }

    def isAllowCountry(self, match: MatchEntity) -> bool:
        return bool(
            {match.getWinner().getCountry(), match.getLooser().getCountry()}.intersection(self.countries)
        )
