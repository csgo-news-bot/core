from src.models import BaseModel
from src.models.Base.HrefBaseModel import HrefBaseModel
from src.models.Base.ImageBaseModel import ImageBaseModel
from src.models.Base.TitleBaseModel import TitleBaseModel


class EventModel(BaseModel, TitleBaseModel, ImageBaseModel, HrefBaseModel):
    __tablename__ = 'event'
    google_storage_folder = 'event'
