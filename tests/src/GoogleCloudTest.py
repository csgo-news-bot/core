import unittest
from google.cloud import storage

from src.service.GoogleCloud import GoogleCloud


class GoogleCloudTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.google_cloud = GoogleCloud()

    def test_exists(self):
        name = 'team/1200px-NAVI_logo1.png'
        exist = storage.Blob(bucket=self.google_cloud.bucket, name=name).exists(self.google_cloud.client)
        self.assertEqual(False, exist)
