from src.abstract.DBConnection import DBConnection
from src.models.TeamModel import TeamModel
from src.models.MatchModel import MatchModel


class TeamCreator(DBConnection):
    def create(self, wonse_score: int, lose_score: int, team_won: TeamModel, team_lose: TeamModel):
        match_model = MatchModel()
        match_model.team_won = team_won
        match_model.team_lose = team_lose

        self.db_connection.add_model(team_lose)
        self.db_connection.commit()
