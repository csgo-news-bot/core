import os
from os.path import dirname


class ConfigService:
    HLTV_SITE = "https://www.hltv.org"
    GOOGLE_STORAGE = "https://storage.googleapis.com/"

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

    @staticmethod
    def get_csgo_server_image_generator_url():
        return os.getenv("CSGO_SERVER_IMAGE_GENERATOR__URL")

    @staticmethod
    def get_app_env():
        return os.getenv("APP_ENV", "prod")

    @staticmethod
    def get_google_storage_bucket():
        return os.getenv("GOOGLE_BUCKET")

    @staticmethod
    def get_url_to_google_cloud(folder: str, image):
        if image == '' or image is None:
            return f'{ConfigService.GOOGLE_STORAGE}{ConfigService.get_google_storage_bucket()}/other/unknown.svg'
        return f'{ConfigService.GOOGLE_STORAGE}{ConfigService.get_google_storage_bucket()}/{folder}/{image}'

    @staticmethod
    def get_url_selenium():
        return os.getenv("SELENIUM_URL")
