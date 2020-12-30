from typing import List

from src.repository.LatestMatchesRepository import LatestMatchesRepository


class LatestMatchesService:
    __repository = None

    def __init__(self):
        self.__repository = LatestMatchesRepository()

    def save(self, list_ids: List):
        self.__repository.save(list_ids)

    def get_all(self) -> List:
        return self.__repository.get_all()
