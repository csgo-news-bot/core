import os
from urllib import parse


class StringHelper:
    @staticmethod
    def get_string(word: str) -> str:
        return f'{word.lower().replace(" ", "_")}'

    @staticmethod
    def get_extension_from_url(url: str) -> str:
        path = parse.urlparse(url).path
        ext = os.path.splitext(path)[1]
        return ext

    @staticmethod
    def search_list_id_in_string(list_ids: list, string: str) -> bool:
        if len(list_ids) == 0:
            return False

        for i in list_ids:
            if f'/{i}/' in string:
                return True

        return False

    @staticmethod
    def get_hashtag(word: str) -> str:
        symbols_list = [" ", "-", "."]
        string = word.lower()
        for i in symbols_list:
            string = string.replace(i, "_")
        return f'#{string}'
