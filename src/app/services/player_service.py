from uuid import UUID, uuid4
from app.models.player import PlayerCreate, PlayerResponse
from app.db.player_repository import PlayerRepository
from typing import List


class PlayerService:
    def __init__(self, repository: PlayerRepository):
        self._repository = repository

    def create_player(self, player_data: PlayerCreate) -> PlayerResponse:
        new_player = PlayerResponse(
            id=uuid4(),
            first_name=player_data.first_name,
            last_name=player_data.last_name,
            dob=player_data.dob,
            position=player_data.position,
            height=player_data.height,
            weight=player_data.weight,
            hits=player_data.hits,
            throws=player_data.throws,
        )

        self._repository.add_player(new_player)
        return new_player

    def get_player_by_id(self, player_id: UUID) -> PlayerResponse | None:
        return self._repository.get_player_by_id(player_id)

    def list_players(self) -> List[PlayerResponse]:
        return self._repository.list_players()
