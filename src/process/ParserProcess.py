import asyncio

from src.abstract.LoggerAbstract import LoggerAbstract
from src.service.parser.HLTVParser import HLTVParser


class ParserProcess(LoggerAbstract):
    async def task(self):
        while True:
            try:
                parser = HLTVParser()
                await parser.execute()
            except Exception as e:
                await self.logger.error(e, exc_info=True)

            await asyncio.sleep(600)  # every 10 min
