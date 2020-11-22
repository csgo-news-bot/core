from typing import Set

from src.repository.LatestMatchesRepository import LatestMatchesRepository


class LatestMatchesService:
    __repository = None

    def __init__(self):
        self.__repository = LatestMatchesRepository()

    def save(self, list_ids: Set):
        self.__repository.save(list_ids)

    def get_all(self) -> Set:
        return self.__repository.get_all()
