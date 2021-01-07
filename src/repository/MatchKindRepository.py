from src.abstract.DBAbstract import DBAbstract
from src.models import MatchKindModel


class MatchKindRepository(DBAbstract):
    def get_by_title(self, title: str) -> MatchKindModel:
        return self.db.query(MatchKindModel).filter(MatchKindModel.title == title).first()
