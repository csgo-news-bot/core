from sqlalchemy import Column, VARCHAR
from sqlalchemy.orm import relationship

from src.models.BaseModel import BaseModel


class EventModel(BaseModel):
    __tablename__ = 'event'

    title = Column(VARCHAR(255), nullable=False)
    match = relationship("MatchModel", uselist=False, back_populates="event")
