import threading
import time

from src.service.publisher.Publisher import Publisher


class PublisherThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            publisher = Publisher()
            publisher.execute()

            time.sleep(1000)  # every 18 min
