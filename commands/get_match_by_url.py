from dotenv import load_dotenv

from src.service.creator.FullMatchCreator import FullMatchCreator
from src.service.parser.CreateMatchDTOFromUrl import CreateMatchDTOFromUrl

load_dotenv()

if __name__ == "__main__":
    a = CreateMatchDTOFromUrl()
    match_dto = a.create('/matches/2346427/paradox-vs-animal-squad-esea-premier-season-36-australia')
    f = FullMatchCreator()
    f.create_from_match_dto(match_dto)
    import time
    time.sleep(999999)

