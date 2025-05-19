from uuid import UUID
from typing import List, Optional
from app.models.player import PlayerCreate, PlayerResponse
from app.services.player_service import PlayerService


class PlayerController:
    def __init__(self, service: PlayerService):
        self.service = service

    def create_player(self, data: PlayerCreate) -> PlayerResponse:
        return self.service.create_player(data)

    def get_player(self, id: UUID) -> Optional[PlayerResponse]:
        return self.service.get_player_by_id(id)

    def list_players(self) -> List[PlayerResponse]:
        return self.service.list_players()
