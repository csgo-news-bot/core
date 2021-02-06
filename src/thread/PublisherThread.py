import threading
import time

from src.abstract.LoggerAbstract import LoggerAbstract
from src.service.publisher.Publisher import Publisher


class PublisherThread(threading.Thread, LoggerAbstract):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
                publisher = Publisher()
                publisher.execute()
            except Exception as e:
                self.logger.error(e, exc_info=True)

            time.sleep(1000)  # every 18 min
