# coding: utf8
import os
import sys
import time

from dotenv import load_dotenv

from src.thread.ParserThread import ParserThread
from src.thread.PublisherThread import PublisherThread

load_dotenv()

PATH = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    parser = ParserThread()
    publisher = PublisherThread()

    parser.start()
    publisher.start()


