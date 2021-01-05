from sqlalchemy import Column, VARCHAR, ForeignKey
from src.models.BaseModel import BaseModel


class TeamModel(BaseModel):
    __tablename__ = 'team'

    name = Column(VARCHAR(255), nullable=False)
