from sqlalchemy import desc, extract
from datetime import datetime
from src.abstract.DBAbstract import DBAbstract
from src.models import MatchModel


class MatchRepository(DBAbstract):
    def get_all(self, limit: int = 10):
        return self.db.query(MatchModel).order_by(desc(MatchModel.created_at)).limit(limit).all()

    def get_all_by_datetime(self, date: datetime):
        return self.db.query(MatchModel).filter(
            extract('month', MatchModel.played_at) == date.month,
            extract('year', MatchModel.played_at) == date.year,
            extract('day', MatchModel.played_at) == date.day
        ).order_by(
            desc(MatchModel.created_at)).all(
        )

    def get_all_by_hltv_list_ids(self, list_ids: list):
        return self.db.query(MatchModel).filter(MatchModel.hltv_id.in_(list_ids)).all()
