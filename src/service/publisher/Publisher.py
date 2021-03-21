import asyncio
import time

from src.abstract.DBAbstract import DBAbstract
from src.abstract.LoggerAbstract import LoggerAbstract
from src.repository.MatchRepository import MatchRepository
from src.service.CountryAllowService import CountryAllowService
from src.service.publisher.core.SenderMessage import SenderMessage
from src.service.updater.MatchUpdater import MatchUpdater


class Publisher(LoggerAbstract, DBAbstract):
    repository: MatchRepository
    sender_message: SenderMessage
    match_updater: MatchUpdater
    country_allow_service: CountryAllowService

    def __init__(self):
        super(Publisher, self).__init__()
        self.repository = MatchRepository()
        self.sender_message = SenderMessage()
        self.match_updater = MatchUpdater()
        self.country_allow_service = CountryAllowService()

    async def execute(self):
        unpublished_matches = self.repository.get_unpublished_matches()
        try:
            if len(unpublished_matches):
                for match in unpublished_matches:
                    if not self.country_allow_service.is_allow_country(match):
                        self.sender_message.execute(match)
                    await self.match_updater.update_publish_by_id(match_id=match.id, publish=True)
                    await asyncio.sleep(3)
                self.db.commit()
                self.logger.info(f'There are new matches {len(unpublished_matches)}')
            else:
                self.logger.info('No matches at this time')
        except Exception as e:
            self.logger.error(e, exc_info=True)
            self.db.rollback()
