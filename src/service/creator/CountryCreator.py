from strict_hint import strict

from src.abstract.DBAbstract import DBAbstract
from src.models import CountryModel
from src.repository.CountryRepository import CountryRepository


class CountryCreator(DBAbstract):
    repository: CountryRepository

    def __init__(self):
        super().__init__()
        self.repository = CountryRepository()

    @strict
    def create(self, title: str = '', short: str = '', commit: bool = False) -> CountryModel:
        assert title != '', 'Country name doesnt be empty'

        country_model = self.repository.get_by_title(title=title)
        if country_model:
            return country_model

        country_model = CountryModel()
        country_model.title = title
        country_model.short = short

        self.db.add_model(country_model, need_flush=True)

        if commit:
            self.db.commit()

        return country_model

