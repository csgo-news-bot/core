from src.abstract.DBAbstract import DBAbstract
from src.models.TeamModel import TeamModel


class TeamCreator(DBAbstract):
    def create(self, title: str, country: int, commit: bool = True) -> TeamModel:
        team_model = TeamModel()
        team_model.title = title
        team_model.country = country

        self.db.add_model(team_model, need_flush=True)

        if commit:
            self.db.commit()

        return team_model

