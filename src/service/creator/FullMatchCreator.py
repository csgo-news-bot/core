import json
import sys
from typing import List
import traceback

from src.abstract.DBAbstract import DBAbstract
from src.abstract.LoggerAbstract import LoggerAbstract
from src.dto.MatchDTO import MatchDTO
from src.repository.MatchRepository import MatchRepository
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
    match_repository: MatchRepository

    def __init__(self):
        super(FullMatchCreator, self).__init__()
        self.country_creator = CountryCreator()
        self.event_creator = EventCreator()
        self.team_creator = TeamCreator()
        self.match_creator = MatchCreator()
        self.match_kind_creator = MatchKindCreator()
        self.match_repository = MatchRepository()

    def create_from_match_dto(self, match_dto: MatchDTO):
        try:
            match = self.match_repository.get_by_hltv_id(match_dto.id)

            if match:
                return None

            country_looser = self.country_creator.create(
                title=match_dto.looser.country,
                image_url=match_dto.looser.country_image_url,
            )
            self.db.commit(flush=True)

            country_winner = self.country_creator.create(
                title=match_dto.winner.country,
                image_url=match_dto.winner.country_image_url,
            )
            self.db.commit(flush=True)

            event = self.event_creator.create(title=match_dto.event)
            team_looser = self.team_creator.create(
                title=match_dto.looser.title,
                country=country_looser,
                image_url=match_dto.looser.image_url
            )
            team_winner = self.team_creator.create(
                title=match_dto.winner.title,
                country=country_winner,
                image_url=match_dto.winner.image_url
            )

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
                href=match_dto.href
            )

            self.db.commit(flush=True)
            self.logger.info(f'Added {match_dto.looser.title} vs {match_dto.winner.title}')
        except Exception as e:
            self.logger.error(f'{e}', exc_info=True)
            self.db.rollback()

    def process_to_create(self, list_of_dtos: List[MatchDTO]):
        for dto in list_of_dtos:
            self.create_from_match_dto(dto)
