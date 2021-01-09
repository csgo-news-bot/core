# coding: utf8
import os
from dotenv import load_dotenv

from src.service.ConfigService import ConfigService
from src.thread.ParserThread import ParserThread
from src.thread.PublisherThread import PublisherThread

load_dotenv()

PATH = os.path.dirname(os.path.abspath(__file__))
config = ConfigService()

if __name__ == "__main__":
    parser = ParserThread()
    parser.start()

    if config.get_app_env() == 'prod':
        publisher = PublisherThread()
        publisher.start()



