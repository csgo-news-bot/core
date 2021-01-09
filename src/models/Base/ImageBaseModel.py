from sqlalchemy import Column, VARCHAR


class ImageBaseModel:
    image = Column(VARCHAR(255), nullable=True)
