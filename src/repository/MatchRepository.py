from typing import List
from uuid import UUID
from sqlalchemy import desc, extract
from sqlalchemy.sql.expression import false
from datetime import datetime

from src.abstract.DBAbstract import DBAbstract
from src.models import MatchModel


class MatchRepository(DBAbstract):
    def get_by_id(self, match_id: UUID) -> MatchModel:
        return self.db.query(MatchModel).filter(MatchModel.id == match_id).first()

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

    def get_unpublished_matches(self) -> List[MatchModel]:
        return self.db.query(MatchModel)\
            .filter(MatchModel.published.is_(None)).order_by(desc(MatchModel.played_at)).all()
