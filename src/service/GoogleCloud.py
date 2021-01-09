from google.cloud import storage

from src.abstract.LoggerAbstract import LoggerAbstract
from src.models import TeamModel, EventModel, CountryModel


class GoogleCloud(LoggerAbstract):
    def __init__(self):
        super(GoogleCloud, self).__init__()
        self.client = storage.Client()

    def upload(self, folder: str, img_name: str) -> bool:
        try:
            assert folder in self.folder_list(), f'{folder} doesnt have access'

            bucket = self.client.get_bucket('csgo_global_elite')
            blob = bucket.blob(f'{folder}/{img_name}')
            blob.upload_from_filename(filename=img_name)

            return True
        except Exception as e:
            self.logger.error(e)
            return False

    @staticmethod
    def folder_list():
        return [
            TeamModel.google_storage_folder,
            EventModel.google_storage_folder,
            CountryModel.google_storage_folder,
        ]
