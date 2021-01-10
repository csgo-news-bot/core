import threading
from abc import ABC

from src.service.singletons.DBConnection import DBConnection
from src.service.DBSession import DBSession


class DBAbstract(ABC):
    db: DBSession

    def __init__(self):
        self.db = DBConnection.db(threading.currentThread().getName())
        super(DBAbstract, self).__init__()
