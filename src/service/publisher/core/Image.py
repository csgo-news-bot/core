from urllib.parse import urlencode

from src.models import MatchModel, TeamModel
from src.service.ConfigService import ConfigService
from src.service.Screenshot import Screenshot


class Image:
    config: ConfigService
    screenshot: Screenshot

    def __init__(self):
        self.config = ConfigService()
        self.screenshot = Screenshot()

    """
    url: https://github.com/shmidtelson/csgo_bot_image_generator
    """

    def get(self, match: MatchModel):
        url = ConfigService.get_csgo_server_image_generator_url()
        params = {
            "team_won_name": match.team_won.title,
            "team_lose_name": match.team_lose.title,
            "championship_name": match.event.title,
            "team_won_score": match.score_won,
            "team_lose_score": match.score_lose,
            "match_type": match.match_kind.title,
            "team_won_logo_url": ConfigService.get_url_to_google_cloud(
                folder=TeamModel.google_storage_folder,
                image=match.team_won.image
            ),
            "team_lose_logo_url": ConfigService.get_url_to_google_cloud(
                folder=TeamModel.google_storage_folder,
                image=match.team_lose.image
            ),
        }
        full_url = f"{url}?{urlencode(params)}"
        image = self.screenshot.take_image(full_url)

        return image
