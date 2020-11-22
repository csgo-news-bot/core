from typing import Set

from src.repository.LatestMatchesRepository import LatestMatchesRepository


class LatestMatchesService:
    repository = None

    def __init__(self):
        self.repository = LatestMatchesRepository()

    def save(self, list_ids: Set):
        self.repository.save(list_ids)

    def get_all(self) -> Set:
        return self.repository.get_all()
