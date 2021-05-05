from typing import List

from src.abstract.DBAbstract import DBAbstract
from src.models import CountryModel


class CountryRepository(DBAbstract):
    def get_by_title(self, title: str) -> CountryModel:
        return self.db.query(CountryModel).filter(CountryModel.title == title).first()

    def get_all(self) -> List[CountryModel]:
        return self.db.query(CountryModel).all()
