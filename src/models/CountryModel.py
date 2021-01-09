from sqlalchemy import Column, VARCHAR

from src.models import BaseModel
from src.models.Base.TitleBaseModel import TitleBaseModel
from src.models.Base.ImageBaseModel import ImageBaseModel


class CountryModel(BaseModel, TitleBaseModel, ImageBaseModel):
    __tablename__ = 'country'
    google_storage_folder = 'country'

    short = Column(VARCHAR(10), nullable=True)
