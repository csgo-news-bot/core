from sqlalchemy.orm import relation
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey

from src.models.TeamModel import TeamModel
from src.models.BaseModel import BaseModel


class MatchModel(BaseModel):
    __tablename__ = 'match'

    team_won = Column(ForeignKey('team.id'), nullable=False, index=True)
    team_lose = Column(ForeignKey('team.id'), nullable=False, index=True)
