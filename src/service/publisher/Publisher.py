from src.abstract.DBAbstract import DBAbstract
from src.abstract.LoggerAbstract import LoggerAbstract
from src.repository.MatchRepository import MatchRepository
from src.service.publisher.core.SenderMessage import SenderMessage
from src.service.updater.MatchUpdater import MatchUpdater


class Publisher(LoggerAbstract, DBAbstract):
    repository: MatchRepository
    sender_message: SenderMessage
    match_updater: MatchUpdater

    def __init__(self):
        super(Publisher, self).__init__()
        self.repository = MatchRepository()
        self.sender_message = SenderMessage()
        self.match_updater = MatchUpdater()

    def execute(self):
        unpublished_matches = self.repository.get_unpublished_matches()
        try:
            if len(unpublished_matches):
                for match in unpublished_matches:
                    result = self.sender_message.execute(match)
                    if result:
                        self.match_updater.update_publish_by_id(match_id=match.id, publish=True)

                self.db.commit()
                self.logger.info(f'There are new matches {len(unpublished_matches)}')
            else:
                self.logger.inf('No matches at this time')
        except Exception as e:
            self.logger.error(e, exc_info=True)
            self.db.rollback()
