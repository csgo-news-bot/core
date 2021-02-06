class TeamDTO:
    BLACKLIST_TEAM_IMAGES_URLS = [
        'https://static.hltv.org/images/team/logo/0',
        '/img/static/team/placeholder.svg'
    ]

    score = None
    title = None
    country = None
    country_image_url = None
    image_url = None

    def set_image_url(self, image_url: str):
        if image_url in self.BLACKLIST_TEAM_IMAGES_URLS:
            return None

        self.image_url = image_url

    def get_image_url(self) -> str:
        return self.image_url
