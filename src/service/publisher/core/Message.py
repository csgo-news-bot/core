from src.models import MatchModel


class Message:
    def get(self, match: MatchModel) -> str:
        list_words = [
            match.team_won.title,
            match.team_lose.title,
            match.team_won.country.title,
            match.team_lose.country.title,
            match.match_kind.title
        ]
        return ' ' + ' '.join(map(lambda x: self.__get_hashtag(x), list_words))

    @staticmethod
    def __get_hashtag(word: str):
        return f'#{word.lower().replace(" ", "_")}'
