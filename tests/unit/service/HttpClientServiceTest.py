import unittest

from src.service.HttpClientService import HttpClientService


class HttpClientServiceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.http_client_service = HttpClientService()
