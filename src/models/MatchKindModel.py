from src.models import BaseModel
from src.models.Base.TitleBaseModel import TitleBaseModel


class MatchKindModel(BaseModel, TitleBaseModel):
    __tablename__ = 'match_kind'
