from sqlalchemy import Column, VARCHAR
from sqlalchemy.orm import relationship

from src.models import BaseModel


class CountryModel(BaseModel):
    __tablename__ = 'country'

    title = Column(VARCHAR(255), nullable=False)
    short = Column(VARCHAR(10), nullable=True)
