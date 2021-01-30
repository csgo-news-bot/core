from strict_hint import strict

from src.abstract.DBAbstract import DBAbstract
from src.models import CountryModel
from src.models.TeamModel import TeamModel
from src.repository.TeamRepository import TeamRepository
from src.service.creator.ImageGoogleCloudCreator import ImageGoogleCloudCreator


class TeamCreator(DBAbstract):
    repository: TeamRepository
    image_google_cloud_creator: ImageGoogleCloudCreator

    def __init__(self):
        super().__init__()
        self.repository = TeamRepository()
        self.image_google_cloud_creator = ImageGoogleCloudCreator()

    @strict
    def create(self, title: str, country: CountryModel, image_url) -> TeamModel:
        assert title != '', 'Team name doesnt be empty'

        team_model = self.repository.get_by_title(title=title)
        if team_model:
            return team_model

        team_model = TeamModel()
        team_model.title = title
        team_model.country = country

        if image_url:
            img_filename = self.image_google_cloud_creator.create(
                image_url=image_url,
                title=title,
                folder=TeamModel.google_storage_folder
            )
            team_model.image = img_filename

        self.db.add_model(team_model)

        return team_model
