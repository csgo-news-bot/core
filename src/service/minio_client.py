import io
import os
from minio import Minio, S3Error

from src.abstract.LoggerAbstract import LoggerAbstract
from src.dto.ImageResponseDTO import ImageResponseDTO
from src.models import TeamModel, EventModel, CountryModel
from src.service.ConfigService import ConfigService


class MinioClient(LoggerAbstract):
    config: ConfigService

    def __init__(self):
        super(MinioClient, self).__init__()
        self.client = Minio(
            os.getenv('MINIO_HOST'),
            access_key=os.getenv('MINIO_ACCESS_KEY'),
            secret_key=os.getenv('MINIO_SECRET_KEY'),
        )
        self.config = ConfigService()

    def upload(self, folder: str, image_response_dto: ImageResponseDTO, img_name) -> bool:
        try:
            assert folder in self.folder_list(), f'{folder} doesnt have access'
            path = f'{folder}/{img_name}'

            try:
                self.client.get_object(
                    os.getenv('MINIO_BUCKET'),
                    path,
                )
            except S3Error as e:
                # Create if not exist
                self.client.put_object(
                    bucket_name=os.getenv('MINIO_BUCKET'),
                    object_name=path,
                    data=io.BytesIO(image_response_dto.blob),
                    length=image_response_dto.length,
                    content_type=image_response_dto.mime
                )
            return True
        except Exception as e:
            self.logger.error(e, exc_info=True)
            return False

    @staticmethod
    def folder_list():
        return [
            TeamModel.google_storage_folder,
            EventModel.google_storage_folder,
            CountryModel.google_storage_folder,
        ]
