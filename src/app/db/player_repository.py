from typing import List, Optional
from uuid import UUID
from app.models.player import PlayerResponse


class PlayerRepository:
    def __init__(self):
        self._players: List[PlayerResponse] = []

    def add_player(self, player: PlayerResponse) -> None:
        self._players.append(player)

    def get_player_by_id(self, player_id: UUID) -> Optional[PlayerResponse]:
        for player in self._players:
            if player.id == player_id:
                return player
        return None

    def list_players(self) -> List[PlayerResponse]:
        return self._players
