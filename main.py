# coding: utf8
import os
from dotenv import load_dotenv
from src.Parser import Parser

load_dotenv()

PATH = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    parser = Parser()
    parser.execute()
