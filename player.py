from dataclasses import dataclass

from countries import COUNTRY_BY_NAME, Country


# TODO: History related functions should be tied to a Player's object state 
@dataclass
class Player:
    """Used to represent the player in leaderboards"""
    name: str = "Default user"
    username: str = "USER"
    country: Country = COUNTRY_BY_NAME["United States"]
    high_score: int = 0

def find_player(players: list[Player], username: str) -> Player | None:
    """Return the player with this username, or None"""
    return next((p for p in players if p.username == username), None)
