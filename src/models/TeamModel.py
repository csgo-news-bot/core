from sqlalchemy import Column, VARCHAR, Integer

from src.models.BaseModel import BaseModel


class TeamModel(BaseModel):
    __tablename__ = 'team'

    title = Column(VARCHAR(255), nullable=False)
    country = Column(Integer, default=0)
