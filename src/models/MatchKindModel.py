from sqlalchemy import Column, VARCHAR

from src.models.BaseModel import BaseModel


class MatchKindModel(BaseModel):
    __tablename__ = 'match_kind'

    title = Column(VARCHAR(255), nullable=False)
