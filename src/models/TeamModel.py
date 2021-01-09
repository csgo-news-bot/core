from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from src.models import BaseModel
from src.models.Base.ImageBaseModel import ImageBaseModel
from src.models.Base.TitleBaseModel import TitleBaseModel


class TeamModel(BaseModel, TitleBaseModel, ImageBaseModel):
    __tablename__ = 'team'
    google_storage_folder = 'team'

    country_id = Column(ForeignKey('country.id'), nullable=False, index=True)
    country = relationship("CountryModel", foreign_keys=[country_id])
