from sqlalchemy import Column, VARCHAR, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.models.BaseModel import BaseModel


class TeamModel(BaseModel):
    __tablename__ = 'team'

    title = Column(VARCHAR(255), nullable=False)

    country_id = Column(ForeignKey('country.id'), nullable=False, index=True)
    country = relationship("CountryModel", foreign_keys=[country_id])
