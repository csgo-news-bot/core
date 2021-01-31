from logging import getLogger
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import sessionmaker, scoped_session

from src.models import BaseModel, Base
from src.service.ConfigService import ConfigService

log = getLogger()


class DBSession:
    _session = None
    _config: ConfigService

    def __init__(self):
        self._config = ConfigService()
        engine = create_engine(
            "postgresql+psycopg2://{}:{}@{}/{}".format(
                self._config.get_db_user(),
                self._config.get_db_pass(),
                self._config.get_db_host(),
                self._config.get_db_table(),
                pool_pre_ping=True
            ),
            pool_recycle=600,
        )
        Base.metadata.create_all(engine)

        session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

        self._session = session()

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

    def flush(self):
        self._session.flush()

    def close_session(self):
        self._session.close()

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
