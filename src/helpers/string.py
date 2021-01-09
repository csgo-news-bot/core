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
