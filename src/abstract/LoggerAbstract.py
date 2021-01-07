from abc import ABC

from src.service.singletons.Logger import Logger


class LoggerAbstract(ABC):
    logger = None

    def __init__(self):
        self.logger = Logger.instance()
