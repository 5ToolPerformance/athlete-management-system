from typing import Dict
from uuid import UUID

db_players: Dict[UUID, dict] = {}


def get_player_by_id(player_id: UUID):
    return db_players.get(player_id)


def save_player(player_data: dict):
    db_players[player_data["id"]] = player_data
    return player_data
