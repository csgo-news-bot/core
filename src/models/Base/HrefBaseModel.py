from sqlalchemy import Column, VARCHAR


class HrefBaseModel:
    href = Column(VARCHAR(500), default="")
