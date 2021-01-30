from strict_hint import strict

from src.abstract.DBAbstract import DBAbstract
from src.models import MatchKindModel
from src.repository.MatchKindRepository import MatchKindRepository


class MatchKindCreator(DBAbstract):
    repository: MatchKindRepository

    def __init__(self):
        super().__init__()
        self.repository = MatchKindRepository()

    @strict
    def create(self, title: str) -> MatchKindModel:
        assert title != '', 'Match kind name doesnt be empty'

        match_kind_model = self.repository.get_by_title(title=title)
        if match_kind_model:
            return match_kind_model

        match_kind_model = MatchKindModel()
        match_kind_model.title = title

        self.db.add_model(match_kind_model)

        return match_kind_model
