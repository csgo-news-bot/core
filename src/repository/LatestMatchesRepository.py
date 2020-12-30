import pickle
from typing import List

from src.service.ConfigService import ConfigService


class LatestMatchesRepository:
    __config = None

    def __init__(self):
        self.__config = ConfigService()

    def save(self, list_ids: List):
        list_ids = list(list_ids)[-100:]

        with open(self.__config.get_latest_matches_file_path(), 'wb') as file:
            pickle.dump(list_ids, file)

    def get_all(self) -> List:
        try:
            with open(self.__config.get_latest_matches_file_path(), 'rb') as file:
                list_ids = pickle.load(file)
        except Exception as e:
            with open(self.__config.get_latest_matches_file_path(), 'wb') as file:
                pickle.dump(set(), file)
            return self.get_all()

        return list_ids
