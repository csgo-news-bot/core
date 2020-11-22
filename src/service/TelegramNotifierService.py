import requests
from src.service.ConfigService import ConfigService


class TelegramNotifierService:
    __config = None

    def __init__(self):
        self.__config = ConfigService()

    def notify(self, message):
        try:
            # TODO: To short this row
            requests.get(
                f'https://api.telegram.org/bot{self.__config.get_telegram_bot_token()}/sendMessage?chat_id={self.__config.get_telegram_receiver_id()}&parse_mode=HTML&text={message}',
                timeout=3.05)
        except Exception:
            pass
