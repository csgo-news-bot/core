from strict_hint import strict

from src.abstract.DBAbstract import DBAbstract
from src.models import EventModel
from src.repository.EventRepository import EventRepository
from src.service.creator.ImageGoogleCloudCreator import ImageGoogleCloudCreator


class EventCreator(DBAbstract):
    repository: EventRepository
    image_google_cloud_creator: ImageGoogleCloudCreator

    def __init__(self):
        super().__init__()
        self.repository = EventRepository()
        self.image_google_cloud_creator = ImageGoogleCloudCreator()

    @strict
    def create(self, title: str, commit: bool = False) -> EventModel:
        assert title != '', 'Event name doesnt be empty'

        event_model = self.repository.get_by_title(title=title)
        if event_model:
            return event_model

        # img_filename = self.image_google_cloud_creator.create(
        #     url=image_url,
        #     title=title,
        #     folder=EventModel.google_storage_folder
        # )

        event_model = EventModel()
        event_model.title = title
        # event_model.image = img_filename

        self.db.add_model(event_model, need_flush=True)

        if commit:
            self.db.commit()

        return event_model
