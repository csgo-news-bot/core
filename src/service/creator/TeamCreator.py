from src.abstract.DBAbstract import DBAbstract
from src.models import CountryModel
from src.models.TeamModel import TeamModel
from src.repository.TeamRepository import TeamRepository


class TeamCreator(DBAbstract):
    repository: TeamRepository

    def __init__(self):
        super().__init__()
        self.repository = TeamRepository()

    def create(self, title: str, country: CountryModel, commit: bool = False) -> TeamModel:
        assert title != '', 'Team name doesnt be empty'

        team_model = self.repository.get_by_title(title=title)
        if team_model:
            return team_model

        team_model = TeamModel()
        team_model.title = title
        team_model.country = country

        self.db.add_model(team_model, need_flush=True)

        if commit:
            self.db.commit()

        return team_model
