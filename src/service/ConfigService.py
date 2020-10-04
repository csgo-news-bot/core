import os
from os.path import dirname


class ConfigService:
    LATEST_MATCHES_PATH = '/var/latest_matches.pickle'
    HLTV_SITE = "https://www.hltv.org"

    def getAppPath(self) -> str:
        return dirname(dirname(dirname(__file__)))

    def getLatestMatechesFilePath(self):
        return self.getAppPath() + self.LATEST_MATCHES_PATH

    def getTelegramBotToken(self):
        return os.getenv("TELEGRAM_BOT_TOKEN")

    def getTelegramRecieverId(self):
        return os.getenv("TELEGRAM_CHAT_ID")

    def getHltvResultEndpoint(self):
        return self.HLTV_SITE + '/results'
