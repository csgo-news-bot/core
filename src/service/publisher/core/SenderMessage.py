from src.models import MatchModel
from src.service.publisher.core.Image import Image
from src.service.publisher.core.TelegramSender import TelegramSender
from src.view.Message import Message


class SenderMessage:
    message: Message
    telegram_sender: TelegramSender
    image: Image

    def __init__(self):
        self.message = Message()
        self.telegram_sender = TelegramSender()
        self.image = Image()

    def execute(self, match: MatchModel) -> bool:
        message = self.message.get(match)
        image = self.image.get(match)
        if image:
            self.telegram_sender.send_image(caption=message, image=image)
            return True

        return False


