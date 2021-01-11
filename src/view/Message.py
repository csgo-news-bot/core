import random
from jinja2 import Template

from src.helpers.string import StringHelper
from src.models import MatchModel
from src.service.ConfigService import ConfigService


class Message:
    def get(self, match: MatchModel) -> str:
        html = open(ConfigService.get_templates_path() + 'message.html').read()

        template = Template(html)

        return template.render(
            match=match,
            stars=self.__get_stars(match.stars),
            hashtags=self.__get_hash_tag_string(match),
            won_phrase=self.__get_random_won_phrase(),
        )

    @staticmethod
    def __get_hash_tag_string(match: MatchModel) -> str:
        list_words = [
            match.team_won.title,
            match.team_lose.title,
            match.team_won.country.title,
            match.team_lose.country.title,
            match.match_kind.title
        ]
        return ' '.join(map(lambda x: StringHelper.get_hashtag(x), list_words))

    @staticmethod
    def __get_stars(count: int) -> str:
        if count:
            return "★" * count
        return ""

    @staticmethod
    def __get_random_won_phrase() -> str:
        words = [
            'нагнули',
            'выйграли у',
            'уделали',
            'натянули',
            'победили у',
            'обыграли',
            'оделели',
            'осилили',
            'разбили',
            'оставили позади',
            'перещеголяли',
            'одержать победу над',
            'взяли верх над',
            'расколотили',
            'сорвали победу у',
        ]
        return random.choice(words)
