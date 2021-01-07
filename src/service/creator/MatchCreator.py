from src.abstract.DBAbstract import DBAbstract
from src.models.EventModel import EventModel
from src.models.TeamModel import TeamModel
from src.models.MatchModel import MatchModel


class MatchCreator(DBAbstract):
    def create(
        self,
        won_score: int,
        lose_score: int,
        team_won: TeamModel,
        team_lose: TeamModel,
        event: EventModel,
        commit: bool = True
    ) -> MatchModel:
        assert lose_score < won_score, f'lose_score ({lose_score}) doesnt be more than won_score ({won_score})'

        match_model = MatchModel()
        match_model.team_won_id = team_won.id
        match_model.team_lose_id = team_lose.id
        match_model.event_id = event.id
        match_model.score_won = won_score
        match_model.score_lose = lose_score

        self.db.add_model(match_model, need_flush=True)

        if commit:
            self.db.commit()

        return match_model
