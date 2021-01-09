from datetime import datetime
from strict_hint import strict

from src.abstract.DBAbstract import DBAbstract
from src.models.EventModel import EventModel
from src.models.TeamModel import TeamModel
from src.models.MatchModel import MatchModel
from src.models.MatchKindModel import MatchKindModel


class MatchCreator(DBAbstract):
    @strict
    def create(
        self,
        won_score: int,
        lose_score: int,
        team_won: TeamModel,
        team_lose: TeamModel,
        event: EventModel,
        match_kind: MatchKindModel,
        played_at: datetime,
        stars: int = 0,
        hltv_id: int = 0,
        href: str = "",
        commit: bool = False,
    ) -> MatchModel:
        assert lose_score < won_score, f'lose_score ({lose_score}) doesnt be more than won_score ({won_score})'
        assert played_at is not None, f'played_at doesnt be is null ({played_at})'
        assert href is not None, f'href doesnt be is null ({played_at})'

        match_model = MatchModel()
        match_model.team_won = team_won
        match_model.team_lose = team_lose
        match_model.event = event
        match_model.score_won = won_score
        match_model.score_lose = lose_score
        match_model.stars = stars
        match_model.played_at = played_at
        match_model.match_kind = match_kind
        match_model.hltv_id = hltv_id
        match_model.href = href

        self.db.add_model(match_model, need_flush=True)

        if commit:
            self.db.commit()

        return match_model
