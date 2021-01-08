import requests

from src.abstract.LoggerAbstract import LoggerAbstract
from src.service.ConfigService import ConfigService


class TelegramSender(LoggerAbstract):
    __config = None

    def __init__(self):
        super(TelegramSender, self).__init__()
        self.__config = ConfigService()

    def send_image(self, image = None, caption: str = ''):
        try:
            url = f"https://api.telegram.org/bot{self.__config.get_telegram_bot_token()}/sendPhoto"
            files = {
                'photo': open(self.__config.get_images_path() + 'image.png', 'rb')
            }
            data = {
                'chat_id': self.__config.get_telegram_receiver_id(),
                'parse_mode': 'HTML',
                'caption': caption
            }
            r = requests.post(url, files=files, data=data, timeout=10)
        except Exception as e:
            self.logger.error(e)
