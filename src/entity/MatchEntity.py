from src.entity.TeamEntity import TeamEntity


class MatchEntity:
    __id = 0
    __winner = None
    __looser = None
    __href = None
    __type = None
    __event = None
    __stars = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setWinner(self, winner: TeamEntity):
        self.__winner = winner

    def getWinner(self) -> TeamEntity:
        return self.__winner

    def setLooser(self, looser: TeamEntity):
        self.__looser = looser

    def getLooser(self) -> TeamEntity:
        return self.__looser

    def setHref(self, href):
        self.__href = href

    def getHref(self):
        return self.__href

    def setType(self, type):
        self.__type = type

    def getType(self):
        return self.__type

    def setEvent(self, event):
        self.__event = event

    def getEvent(self):
        return self.__event

    def setStars(self, stars):
        self.__stars = stars

    def getStars(self):
        return self.__stars

