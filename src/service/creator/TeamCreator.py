from src.abstract.DBConnection import DBConnection
from src.models.TeamModel import TeamModel


class TeamCreator(DBConnection):
    def create(self):
        team_model = TeamModel()
        team_model.name = 'test'

        self.db_connection.add_model(team_model)
        self.db_connection.commit()
