from strict_hint import strict

from src.abstract.DBAbstract import DBAbstract
from src.models import CountryModel
from src.repository.CountryRepository import CountryRepository
from src.service.ConfigService import ConfigService
from src.service.creator.image_storage_creator import ImageStorageCreator


class CountryCreator(DBAbstract):
    repository: CountryRepository
    image_storage_creator: ImageStorageCreator
    config: ConfigService

    def __init__(self):
        super().__init__()
        self.repository = CountryRepository()
        self.image_storage_creator = ImageStorageCreator()
        self.config = ConfigService()

    @strict
    def create(self, image_url: str = None, title: str = '', short: str = '', commit: bool = False) -> CountryModel:
        assert title != '', 'Country name doesnt be empty'

        country_model = self.repository.get_by_title(title=title)
        if country_model:
            return country_model

        img_filename = self.image_storage_creator.create(
            image_url=self.config.HLTV_SITE + image_url,
            title=title,
            folder=CountryModel.google_storage_folder
        )

        country_model = CountryModel()
        country_model.title = title
        country_model.short = short
        country_model.image = img_filename

        self.db.add_model(country_model, need_flush=True)

        return country_model
