import re

from math import prod
from typing import Dict, List, Tuple


def get_min_required_set(sessions: List[str]) -> Dict[str, int]:
    min_set = {"red": 0, "blue": 0, "green": 0}
    for handful in [session.split(",") for session in sessions.split(";")]:
        for entry in handful:
            n, colour = re.sub("[^a-zA-Z0-9\s]", "", entry).strip().split()
            min_set[colour] = max(min_set[colour], int(n))
    return min_set
            

def game_is_possible(min_set: Dict[str, int]) -> bool:
    limit = {
        "red": 12,
        "green": 13,
        "blue": 14,
        }

    impossible = False

    for colour, n in min_set.items():
        if n > limit[colour]:
            impossible = True
            break 
    return impossible


if __name__ == "__main__":
    import os
    from pathlib import Path 

    filename = "input"

    try:
        filepath = Path(__file__).parent.resolve() / filename
    except:
        filepath = Path(os.getcwd()) / filename

    file = open(filepath, "r")

    possible_games_ids = []
    total_power = 0
    while line:= file.readline():
        game, sessions = line.split(":")
        game_id = int(game.strip().split()[-1])
        min_set = get_min_required_set(sessions)

        power = prod(min_set.values())
        total_power += power

        impossible = game_is_possible(min_set)
        if not impossible:
            possible_games_ids.append(game_id)

        # print(f"Game {game_id} is impossible: {impossible}. Required set {min_set}")

    file.close()
    print(f"[Part 1] Possible game {sum(possible_games_ids)}")
    print(f"[Part 2] Total power: {total_power}")
