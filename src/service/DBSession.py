from logging import getLogger
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import Session, sessionmaker

from src.models import BaseModel
from src.service.ConfigService import ConfigService

log = getLogger()


class DBSession:
    _session: Session

    def __init__(self):
        self.config = ConfigService()

        session_class = sessionmaker(
            bind=create_engine(
                "postgresql+psycopg2://{}:{}@{}/{}".format(
                    self.config.get_db_user(),
                    self.config.get_db_pass(),
                    self.config.get_db_host(),
                    self.config.get_db_table(),
                )
            )
        )
        self._session = session_class()

    def add_model(self, model: BaseModel, need_flush: bool = False):
        self._session.add(model)

        if need_flush:
            self._session.flush([model])

        return model

    def delete_model(self, model: BaseModel):
        if model is None:
            log.warning(f'{__name__}: model is None')

        try:
            self._session.delete(model)
        except IntegrityError as e:
            log.error(f'`{__name__}` {e}')
        except DataError as e:
            log.error(f'`{__name__}` {e}')

    def query(self, *entities, **kwargs):
        return self._session.query(*entities, **kwargs)

    def rollback(self):
        self._session.rollback()

    def commit(self, flush: bool = False, need_close: bool = False):
        try:
            self._session.commit()
        except IntegrityError as e:
            log.error(f'`{__name__}` {e}')
            raise
        except DataError as e:
            log.error(f'`{__name__}` {e}')
            raise

        if flush:
            self._session.flush()

        if need_close:
            self.close()

    def close(self):
        try:
            self.close()
        except IntegrityError as e:
            log.error(f'`{__name__}` {e}')
            raise
        except DataError as e:
            log.error(f'`{__name__}` {e}')
            raise

    def __del__(self):
        self._session.close()
