from datetime import datetime

from src.dto.TeamDTO import TeamDTO


class MatchDTO:
    id: int = 0
    stars: int = None
    href: str = None
    type: str = None
    event: str = None
    winner: TeamDTO = None
    looser: TeamDTO = None
    played_at: datetime = None
