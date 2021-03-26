import os
import sys
import logging
import logging as handlers

import tg_logger


class Logger:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = logging.getLogger('app')
            cls._instance.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s: [%(filename)s] - %(name)s - %(levelname)s - %(message)s')

            log_handler = handlers.StreamHandler(stream=sys.stdout)
            log_handler.setFormatter(formatter)

            cls._instance.addHandler(log_handler)

        return cls._instance


class TelegramLogger:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = logging.getLogger('app.tg')
            cls._instance.setLevel(logging.ERROR)

            tg_logger.setup(
                cls._instance,
                token=os.getenv('TELEGRAM_LOGGER_BOT_TOKEN'),
                users=[int(os.getenv('TELEGRAM_LOGGER_CHAT_ID'))]
            )

        return cls._instance
