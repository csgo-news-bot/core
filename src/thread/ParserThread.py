import threading
import time

from src.abstract.LoggerAbstract import LoggerAbstract
from src.service.parser.HLTVParser import HLTVParser


class ParserThread(threading.Thread, LoggerAbstract):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
                parser = HLTVParser()
                parser.execute()
            except Exception as e:
                self.logger.error(e, exc_info=True)

            time.sleep(600)  # every 10 min
