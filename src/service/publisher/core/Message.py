import random
from src.models import MatchModel


class Message:
    def get(self, match: MatchModel) -> str:
        return f"""
        {self.__get_stars(match.stars)}<b>{match.team_won.title}</b> {self.__get_random_won_phrase()} 
        {match.team_lose.title} со счетом <b>{match.score_won}</b> - {match.score_lose} ({match.match_kind.title}) 
        на турнире {match.event.title}, подробнее <a href='{match.href}'>здесь</a> \n\n
        {self.__get_hash_tag_string(match)}
        """

    def __get_hash_tag_string(self, match: MatchModel) -> str:
        list_words = [
            match.team_won.title,
            match.team_lose.title,
            match.team_won.country.title,
            match.team_lose.country.title,
            match.match_kind.title
        ]
        return ' ' + ' '.join(map(lambda x: self.__get_hashtag(x), list_words))

    @staticmethod
    def __get_stars(count: int) -> str:
        if count:
            return "★" * count + " "
        return ""

    @staticmethod
    def __get_hashtag(word: str) -> str:
        return f'#{word.lower().replace(" ", "_")}'

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
            'разбоставили позади',
            'перещеголяли',
            'одержать победу над',
            'взяли верх над',
            'расколотили',
            'сорвали победу у ',
        ]
        return random.choice(words)
