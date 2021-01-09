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
            for match in unpublished_matches:
                self.sender_message.execute(match)
                self.match_updater.update_publish_by_id(match_id=match.id, publish=True)

            self.db.commit()
        except Exception as e:
            self.logger.error(e)
            self.db.rollback()