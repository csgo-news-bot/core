from sqlalchemy import Column, ForeignKey, SmallInteger, Integer, VARCHAR, TIMESTAMP, Boolean
from sqlalchemy.orm import relationship

from src.models.BaseModel import BaseModel


class MatchModel(BaseModel):
    __tablename__ = 'match'

    played_at = Column(TIMESTAMP, nullable=True, default=None)

    team_won_id = Column(ForeignKey('team.id'), nullable=False, index=True)
    team_won = relationship("TeamModel", foreign_keys=[team_won_id])
    team_lose_id = Column(ForeignKey('team.id'), nullable=False, index=True)
    team_lose = relationship("TeamModel", foreign_keys=[team_lose_id])

    event_id = Column(ForeignKey('event.id'), nullable=False, index=True)
    event = relationship("EventModel", foreign_keys=[event_id])

    match_kind_id = Column(ForeignKey('match_kind.id'), nullable=False, index=True)
    match_kind = relationship("MatchKindModel", foreign_keys=[match_kind_id])

    score_lose = Column(SmallInteger, default=0)
    score_won = Column(SmallInteger, default=0)
    stars = Column(SmallInteger, default=0)
    hltv_id = Column(Integer, default=0)
    href = Column(VARCHAR(500), default="")
    published = Column(Boolean, default=None)
