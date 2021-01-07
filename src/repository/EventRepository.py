from src.abstract.DBAbstract import DBAbstract
from src.models import EventModel


class EventRepository(DBAbstract):
    def get_by_title(self, title: str) -> EventModel:
        return self.db.query(EventModel).filter(EventModel.title == title).first()
