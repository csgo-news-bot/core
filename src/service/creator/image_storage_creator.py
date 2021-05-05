from strict_hint import strict

from src.helpers.string import StringHelper
from src.service.ConfigService import ConfigService
from src.service.HttpClientService import HttpClientService
from src.service.minio_client import MinioClient


class ImageStorageCreator:
    storage_client: MinioClient
    config: ConfigService
    http_client_service: HttpClientService

    def __init__(self):
        self.storage_client = MinioClient()
        self.config = ConfigService()
        self.http_client_service = HttpClientService()

    @strict
    def create(self, image_url: str, title, folder: str) -> str:
        image_response_dto = self.http_client_service.get_blob_from_url(
            image_url
        )

        img_title = StringHelper.get_string(title)
        img_filename = img_title + image_response_dto.ext

        self.storage_client.upload(
            folder=folder,
            image_response_dto=image_response_dto,
            img_name=img_filename
        )

        return img_filename
