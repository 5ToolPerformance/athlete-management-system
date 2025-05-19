import json
from uuid import UUID
from datetime import date
from app.controller.player_controller import PlayerController
from app.services.player_service import PlayerService
from app.db.player_repository import PlayerRepository
from app.models.player import PlayerCreate

controller = PlayerController(PlayerService(PlayerRepository()))


def create_player():
    try:
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        dob = input("Date of Birth (): ").strip()
        position = input("Position: ").strip()
        height = input("Height (in): ").strip()
        weight = input("Weight (lbs): ").strip()
        hits = input("Hits (Right/Left/Switch): ").strip()
        throws = input("Throws (Right/Left): ").strip()

        player_data = PlayerCreate(
            first_name=first_name,
            last_name=last_name,
            dob=date.fromisoformat(dob),
            position=position,
            height=height,
            weight=weight,
            hits=hits,
            throws=throws,
        )
        player = controller.create_player(player_data)
        print(f"\n✅ Player created: {player}")
    except Exception as e:
        print(f"❌ Error creating player: {e}")


def list_players():
    players = controller.list_players()
    print("\n📋 Players:")
    for player in players:
        print(player)


def export_players_to_json(filename="players_export.json"):
    try:
        players = controller.list_players()
        players_data = [p.dict() for p in players]
        with open(filename, "w") as f:
            json.dump(players_data, f, default=str, indent=4)
        print(f"\n✅ Exported {len(players)} players to {filename}")
    except Exception as e:
        print(f"❌ Error exporting players: {e}")


def player_cli_menu():
    while True:
        print("\n--- Player CLI ---")
        print("1. Create Player")
        print("2. List Players")
        print("3. Export Players to JSON")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_player()
        elif choice == "2":
            list_players()
        elif choice == "3":
            export_players_to_json()
        elif choice == "4":
            print("👋 Exiting Player CLI")
            break
        else:
            print("❌ Invalid option. Try again.")
