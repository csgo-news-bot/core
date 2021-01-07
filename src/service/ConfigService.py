import os
from os.path import dirname


class ConfigService:
    LATEST_MATCHES_PATH = '/var/latest_matches.pickle'
    HLTV_SITE = "https://www.hltv.org"

    def get_latest_matches_file_path(self):
        return self.get_app_path() + self.LATEST_MATCHES_PATH

    def get_hltv_result_endpoint(self):
        return self.HLTV_SITE + '/results'

    @staticmethod
    def get_app_path() -> str:
        return dirname(dirname(dirname(__file__)))

    @staticmethod
    def get_telegram_bot_token():
        return os.getenv("TELEGRAM_BOT_TOKEN")

    @staticmethod
    def get_telegram_receiver_id():
        return os.getenv("TELEGRAM_CHAT_ID")

    @staticmethod
    def get_db_user():
        return os.getenv("DB_USER")

    @staticmethod
    def get_db_pass():
        return os.getenv("DB_PASS")

    @staticmethod
    def get_db_host():
        return os.getenv("DB_HOST")

    @staticmethod
    def get_db_table():
        return os.getenv("DB_TABLE")
