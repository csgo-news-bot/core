from sqlalchemy import Column, VARCHAR


class TitleBaseModel:
    title = Column(VARCHAR(255), nullable=False)
