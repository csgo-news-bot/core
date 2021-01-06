from sqlalchemy import Column, ForeignKey, SmallInteger, Integer, VARCHAR

from src.models.BaseModel import BaseModel


class MatchModel(BaseModel):
    __tablename__ = 'match'

    team_won_id = Column(ForeignKey('team.id'), nullable=False, index=True)
    team_lose_id = Column(ForeignKey('team.id'), nullable=False, index=True)
    event_id = Column(ForeignKey('event.id'), nullable=False, index=True)
    score_lose = Column(SmallInteger, default=0)
    score_won = Column(SmallInteger, default=0)
    stars = Column(SmallInteger, default=0)
    type = Column(SmallInteger, default=0)
    hltv_id = Column(Integer, default=0)
    href = Column(VARCHAR(500), default="")
