import pickle
from typing import Set

from src.service.ConfigService import ConfigService


class LatestMatchesRepository:
    config = None

    def __init__(self):
        self.config = ConfigService()

    def save(self, listIds: Set):
        listIds = list(listIds)[-100:]

        with open(self.config.getLatestMatechesFilePath(), 'wb') as file:
            pickle.dump(set(listIds), file)

    def getAll(self) -> Set:
        try:
            with open(self.config.getLatestMatechesFilePath(), 'rb') as file:
                listIds = pickle.load(file)
        except:
            with open(self.config.getLatestMatechesFilePath(), 'wb') as file:
                pickle.dump(set(), file)
            return self.getAll()

        return listIds
