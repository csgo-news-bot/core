from strict_hint import strict

from src.helpers.string import StringHelper
from src.service.ConfigService import ConfigService
from src.service.GoogleCloud import GoogleCloud
from src.service.HttpClientService import HttpClientService


class ImageGoogleCloudCreator:
    google_cloud: GoogleCloud
    config: ConfigService
    http_client_service: HttpClientService

    def __init__(self):
        self.google_cloud = GoogleCloud()
        self.config = ConfigService()
        self.http_client_service = HttpClientService()

    @strict
    def create(self, url: str, title, folder: str) -> str:
        img_full_url = self.config.HLTV_SITE + url
        img_blob = self.http_client_service.get_blob_from_url(
            img_full_url
        )

        img_title = StringHelper.get_string(title)
        img_ext = StringHelper.get_extension_from_url(img_full_url)
        img_filename = img_title + img_ext

        self.google_cloud.upload(
            folder=folder,
            img_blob=img_blob,
            img_name=img_filename
        )

        return img_filename
