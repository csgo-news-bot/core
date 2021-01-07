from src.abstract.DBAbstract import DBAbstract
from src.models import TeamModel


class TeamRepository(DBAbstract):
    def get_by_title(self, title: str) -> TeamModel:
        return self.db.query(TeamModel).filter(TeamModel.title == title).first()
