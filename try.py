import telegram
from dotenv import load_dotenv

from src.service.parser.HLTVParser import HLTVParser

load_dotenv()


if __name__ == "__main__":
    parser = HLTVParser()
    for i in range(1, 500000):
        parser.execute(page=i, default_published_match=True)
    # a = CreateMatchDTOFromUrl()
    # match_dto = a.create('/matches/2346295/pain-vs-rebirth-dreamhack-open-january-2021-north-america')
    # f = FullMatchCreator()
    # f.create_from_match_dto(match_dto)

