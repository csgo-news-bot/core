import asyncio

from src.abstract.LoggerAbstract import LoggerAbstract
from src.service.publisher.Publisher import Publisher


class PublisherProcess(LoggerAbstract):
    async def task(self):
        while True:
            try:
                publisher = Publisher()
                await publisher.execute()
            except Exception as e:
                self.logger.error(e, exc_info=True)

            await asyncio.sleep(1000)  # every 18 min
