from uuid import UUID

from src.abstract.DBAbstract import DBAbstract
from src.repository.MatchRepository import MatchRepository


class MatchUpdater(DBAbstract):
    repository: MatchRepository

    def __init__(self):
        super(MatchUpdater, self).__init__()
        self.repository = MatchRepository()

    async def update_publish_by_id(self, match_id: UUID, publish: bool, commit: bool = False):
        match_model = self.repository.get_by_id(match_id)

        match_model.published = publish

        if commit:
            await self.db.commit()
