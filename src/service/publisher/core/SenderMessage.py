from src.models import MatchModel
from src.service.publisher.core.Image import Image
from src.service.publisher.core.Message import Message
from src.service.publisher.core.TelegramSender import TelegramSender


class SenderMessage:
    message: Message
    telegram_sender: TelegramSender
    image: Image

    def __init__(self):
        self.message = Message()
        self.telegram_sender = TelegramSender()
        self.image = Image()

    def execute(self, match: MatchModel):
        message = self.message.get(match)
        image = self.image.get(match)
        self.telegram_sender.send_image(caption=message, image=image)


