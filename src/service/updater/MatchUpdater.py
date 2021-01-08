from uuid import UUID

from src.abstract.DBAbstract import DBAbstract
from src.repository.MatchRepository import MatchRepository


class MatchUpdater(DBAbstract):
    repository: MatchRepository

    def __init__(self):
        super(MatchUpdater, self).__init__()
        self.repository = MatchRepository()

    def update_publish_by_id(self, match_id: UUID, publish: bool, commit: bool = False):
        match_model = self.repository.get_by_id(match_id)

        match_model.published = publish

        self.db.add_model(match_model, need_flush=True)

        if commit:
            self.db.commit()

        return match_model
