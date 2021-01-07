# coding: utf8
import os
import time
from dotenv import load_dotenv
from src.service.parser.HLTVParser import HLTVParser

load_dotenv()

PATH = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    while True:
        parser = HLTVParser()
        parser.execute()
        time.sleep(600)  # every 20 min
