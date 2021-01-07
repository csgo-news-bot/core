from sqlalchemy import Column, ForeignKey, SmallInteger, Integer, VARCHAR
from sqlalchemy.orm import relationship

from src.models.BaseModel import BaseModel


class MatchModel(BaseModel):
    __tablename__ = 'match'

    team_won_id = Column(ForeignKey('team.id'), nullable=False, index=True)
    team_won = relationship("TeamModel", foreign_keys=[team_won_id])
    team_lose_id = Column(ForeignKey('team.id'), nullable=False, index=True)
    team_lose = relationship("TeamModel", foreign_keys=[team_lose_id])

    event_id = Column(ForeignKey('event.id'), nullable=False, index=True)
    event = relationship("EventModel", back_populates="match")

    score_lose = Column(SmallInteger, default=0)
    score_won = Column(SmallInteger, default=0)
    stars = Column(SmallInteger, default=0)
    type = Column(SmallInteger, default=0)
    hltv_id = Column(Integer, default=0)
    href = Column(VARCHAR(500), default="")
