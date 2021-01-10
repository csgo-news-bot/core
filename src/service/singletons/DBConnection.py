from src.service.DBSession import DBSession


class DBConnection:
    SESSIONS_KEYS_LIST = [
        'publisher',
        'parser',
    ]
    _instance: dict = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def db(cls, session_name: str):
        if cls._instance is None:
            cls._instance = {
                DBConnection.SESSIONS_KEYS_LIST[0]: DBSession(),
                DBConnection.SESSIONS_KEYS_LIST[1]: DBSession(),
            }
        return cls._instance.get(session_name)
