from sqlalchemy import desc

from src.abstract.DBAbstract import DBAbstract
from src.models import MatchModel


class MatchRepository(DBAbstract):
    def get_all(self, limit: int = 10):
        return self.db.query(MatchModel).order_by(desc(MatchModel.created_at)).limit(limit).all()
