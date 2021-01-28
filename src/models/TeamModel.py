from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from src.models import BaseModel, CountryModel
from src.models.Base.HrefBaseModel import HrefBaseModel
from src.models.Base.ImageBaseModel import ImageBaseModel
from src.models.Base.TitleBaseModel import TitleBaseModel


class TeamModel(BaseModel, TitleBaseModel, ImageBaseModel, HrefBaseModel):
    __tablename__ = 'team'
    google_storage_folder = 'team'

    country_id = Column(ForeignKey('country.id'), nullable=False, index=True)
    country: CountryModel = relationship(
        "CountryModel",
        foreign_keys=[country_id],
        viewonly=True
    )
