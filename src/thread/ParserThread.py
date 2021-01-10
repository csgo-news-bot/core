import threading
import time

from src.service.parser.HLTVParser import HLTVParser


class ParserThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            parser = HLTVParser()
            parser.execute()
            time.sleep(600)  # every 20 min
