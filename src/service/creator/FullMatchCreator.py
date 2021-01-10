import json
import sys
from typing import List
import traceback

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

    def process_to_create(self, list_of_dtos: List[MatchDTO], black_list: List[int] = None):
        for dto in list_of_dtos:
            if dto.id in black_list:
                continue
            try:
                country_looser = self.country_creator.create(
                    title=dto.looser.country,
                    image_url=dto.looser.country_image_url,
                    commit=True
                )

                country_winner = self.country_creator.create(
                    title=dto.winner.country,
                    image_url=dto.winner.country_image_url,
                    commit=True
                )

                event = self.event_creator.create(title=dto.event)
                team_looser = self.team_creator.create(
                    title=dto.looser.title,
                    country=country_looser,
                    image_url=dto.looser.image_url
                )
                team_winner = self.team_creator.create(
                    title=dto.winner.title,
                    country=country_winner,
                    image_url=dto.winner.image_url
                )
                match_kind = self.match_kind_creator.create(title=dto.type)
                match = self.match_creator.create(
                    team_won=team_winner,
                    team_lose=team_looser,
                    match_kind=match_kind,
                    event=event,

                    won_score=int(dto.winner.score),
                    lose_score=int(dto.looser.score),
                    played_at=dto.played_at,
                    stars=dto.stars,
                    hltv_id=dto.id,
                    href=dto.href
                )

                self.db.commit(flush=True)
                self.logger.info(f'Added {dto.looser.title} vs {dto.winner.title}')
            except Exception as e:
                self.logger.error(f'{e}', exc_info=True)
                self.db.rollback()

