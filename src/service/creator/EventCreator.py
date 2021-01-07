from src.abstract.DBAbstract import DBAbstract
from src.models import EventModel


class EventCreator(DBAbstract):
    def create(self, title: str, commit: bool = True) -> EventModel:
        event_model = EventModel()
        event_model.title = title

        self.db.add_model(event_model, need_flush=True)

        if commit:
            self.db.commit()

        return event_model
