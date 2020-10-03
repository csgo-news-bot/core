from typing import Set

from src.repository.LatestMatchesRepository import LatestMatchesRepository


class LatestMatchesService:
    repository = None

    def __init__(self):
        self.repository = LatestMatchesRepository()

    def save(self, listIds: Set):
        self.repository.save(listIds)

    def getAll(self) -> Set:
        return self.repository.getAll()
