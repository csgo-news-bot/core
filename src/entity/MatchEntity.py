from src.entity.TeamEntity import TeamEntity


class MatchEntity:
    __id: int = 0
    __stars: int = None
    __href: str = None
    __type: str = None
    __event: str = None
    __winner: TeamEntity = None
    __looser: TeamEntity = None

    def set_id(self, identifier: int):
        self.__id = identifier

    def get_id(self):
        return self.__id

    def set_winner(self, winner: TeamEntity):
        self.__winner = winner

    def get_winner(self) -> TeamEntity:
        return self.__winner

    def set_looser(self, looser: TeamEntity):
        self.__looser = looser

    def get_looser(self) -> TeamEntity:
        return self.__looser

    def set_href(self, href: str):
        self.__href = href

    def get_href(self) -> str:
        return self.__href

    def set_type(self, kind: str):
        self.__type = kind

    def get_type(self) -> str:
        return self.__type

    def set_event(self, event: str):
        self.__event = event

    def get_event(self) -> str:
        return self.__event

    def set_stars(self, stars: int):
        self.__stars = stars

    def get_stars(self) -> int:
        return self.__stars
