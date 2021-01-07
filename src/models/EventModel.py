from sqlalchemy import Column, VARCHAR

from src.models.BaseModel import BaseModel


class EventModel(BaseModel):
    __tablename__ = 'event'

    title = Column(VARCHAR(255), nullable=False)
