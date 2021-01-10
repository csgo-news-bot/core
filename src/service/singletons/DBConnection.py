from src.service.DBSession import DBSession


class DBConnection:
    _instance: dict = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def db(cls, session_name: str):
        if cls._instance is None:
            cls._instance = {
                'parser': DBSession(),
                'publisher': DBSession(),
            }
        return cls._instance.get(session_name)
