from typing import List

from src.abstract.DBAbstract import DBAbstract
from src.abstract.LoggerAbstract import LoggerAbstract
from src.dto.MatchDTO import MatchDTO
from src.service.creator.CountryCreator import CountryCreator
from src.service.creator.EventCreator import EventCreator
from src.service.creator.MatchCreator import MatchCreator
from src.service.creator.MatchKindCreator import MatchKindCreator
from src.service.creator.TeamCreator import TeamCreator


class FullMatchCreator(DBAbstract, LoggerAbstract):
    country_creator: CountryCreator
    event_creator: EventCreator
    team_creator: TeamCreator
    match_creator: MatchCreator
    match_kind_creator: MatchKindCreator

    def __init__(self):
        super(FullMatchCreator, self).__init__()
        self.country_creator = CountryCreator()
        self.event_creator = EventCreator()
        self.team_creator = TeamCreator()
        self.match_creator = MatchCreator()
        self.match_kind_creator = MatchKindCreator()

    def create_from_match_dto(self, match_dto: MatchDTO, default_published_match: bool = None):
        country_looser = self.country_creator.create(
            title=match_dto.looser.country,
            image_url=match_dto.looser.country_image_url,
        )

        country_winner = self.country_creator.create(
            title=match_dto.winner.country,
            image_url=match_dto.winner.country_image_url,
        )

        team_looser = self.team_creator.create(
            title=match_dto.looser.title,
            country=country_looser,
            image_url=match_dto.looser.image_url,
        )
        team_winner = self.team_creator.create(
            title=match_dto.winner.title,
            country=country_winner,
            image_url=match_dto.winner.image_url,
        )

        event = self.event_creator.create(title=match_dto.event)
        match_kind = self.match_kind_creator.create(title=match_dto.type)

        match = self.match_creator.create(
            team_won=team_winner,
            team_lose=team_looser,
            match_kind=match_kind,
            event=event,

            won_score=int(match_dto.winner.score),
            lose_score=int(match_dto.looser.score),
            played_at=match_dto.played_at,
            stars=match_dto.stars,
            hltv_id=match_dto.id,
            href=match_dto.href,
            published=default_published_match
        )

        self.logger.info(f'Added {match_dto.looser.title} vs {match_dto.winner.title}')
        self.db.commit(flush=True)

    def process_to_create(self, list_of_dtos: List[MatchDTO], default_published_match: bool = None):
        for dto in list_of_dtos:
            self.create_from_match_dto(dto, default_published_match=default_published_match)
