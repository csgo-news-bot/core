from strict_hint import strict

from src.abstract.DBAbstract import DBAbstract
from src.models import CountryModel
from src.models.TeamModel import TeamModel
from src.repository.TeamRepository import TeamRepository
from src.service.creator.image_storage_creator import ImageStorageCreator


class TeamCreator(DBAbstract):
    repository: TeamRepository
    image_storage_creator: ImageStorageCreator

    def __init__(self):
        super().__init__()
        self.repository = TeamRepository()
        self.image_storage_creator = ImageStorageCreator()

    @strict
    def create(self, title: str, country: CountryModel, image_url) -> TeamModel:
        assert title != '', 'Team name doesnt be empty'

        team_model = self.repository.get_by_title(title=title)
        if team_model:
            self.__change_team_country_if_it_changed(team_model, country)
            return team_model

        team_model = TeamModel()
        team_model.title = title
        team_model.country = country

        if image_url:
            img_filename = self.image_storage_creator.create(
                image_url=image_url,
                title=title,
                folder=TeamModel.google_storage_folder
            )
            team_model.image = img_filename

        self.db.add_model(team_model, need_flush=True)

        return team_model

    def __change_team_country_if_it_changed(self, team_model: TeamModel, country_model: CountryModel):
        if team_model.country.title != country_model.title:
            team_model.country = country_model
            self.db.add_model(team_model, need_flush=True)
