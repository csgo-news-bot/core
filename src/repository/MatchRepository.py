import datetime as datetime
from sqlalchemy import desc
from datetime import datetime
from src.abstract.DBAbstract import DBAbstract
from src.models import MatchModel


class MatchRepository(DBAbstract):
    def get_all(self, limit: int = 10):
        return self.db.query(MatchModel).order_by(desc(MatchModel.created_at)).limit(limit).all()

    def get_all_by_datetime(self, date: datetime):
        return self.db.query(MatchModel).filter_by(played_at=date).order_by(desc(MatchModel.created_at)).all()
