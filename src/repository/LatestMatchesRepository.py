import pickle
from typing import Set

from src.service.ConfigService import ConfigService


class LatestMatchesRepository:
    config = None

    def __init__(self):
        self.config = ConfigService()

    def save(self, list_ids: Set):
        list_ids = list(list_ids)[-100:]

        with open(self.config.get_latest_matches_file_path(), 'wb') as file:
            pickle.dump(set(list_ids), file)

    def get_all(self) -> Set:
        try:
            with open(self.config.get_latest_matches_file_path(), 'rb') as file:
                list_ids = pickle.load(file)
        except Exception:
            with open(self.config.get_latest_matches_file_path(), 'wb') as file:
                pickle.dump(set(), file)
            return self.get_all()

        return list_ids
