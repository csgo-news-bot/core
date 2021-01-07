from src.abstract.DBAbstract import DBAbstract
from src.models import MatchModel


class MatchRepository(DBAbstract):
    def get_all(self, limit: int):
        return self.db.query(MatchModel).all()
