from abc import ABC
from src.service.DBSession import DBSession


class DBConnection(ABC):
    def __init__(self):
        self.db_connection = DBSession()
