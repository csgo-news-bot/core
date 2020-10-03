import requests
from src.service.ConfigService import ConfigService


class TelegramNotifierService:
    def __init__(self):
        self.config = ConfigService()

    def notify(self, message):
        try:
            requests.get(f'https://api.telegram.org/bot{self.config.getTelegramBotToken()}/sendMessage?chat_id={self.config.getTelegramRecieverId()}&parse_mode=HTML&text={message}', timeout=3.05)
        except Exception as e:
            pass
