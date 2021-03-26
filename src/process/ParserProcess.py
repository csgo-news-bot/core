import asyncio

from src.abstract.LoggerAbstract import LoggerAbstract
from src.service.parser.HLTVParser import HLTVParser
from src.service.singletons.Logger import TelegramLogger


class ParserProcess(LoggerAbstract):
    async def task(self):
        while True:
            try:
                parser = HLTVParser()
                parser.execute()
            except Exception as e:
                self.logger.error(e, exc_info=True)
                TelegramLogger.instance().error(str(e))

            await asyncio.sleep(600)  # every 10 min
