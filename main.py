# coding: utf8
import asyncio
import os

from dotenv import load_dotenv

from src.process.ParserProcess import ParserProcess
from src.process.PublisherProcess import PublisherProcess
from src.service.ConfigService import ConfigService
load_dotenv()

PATH = os.path.dirname(os.path.abspath(__file__))
config = ConfigService()

task_parser = ParserProcess()
task_publisher = PublisherProcess()

if __name__ == "__main__":
    io_loop = asyncio.get_event_loop()
    tasks = [
        io_loop.create_task(task_parser.task(), name="parser"),
    ]

    if config.get_app_env() == 'prod':
        tasks.append(io_loop.create_task(task_publisher.task(), name="publisher"))

    io_loop.run_until_complete(asyncio.wait(tasks))
    io_loop.close()


