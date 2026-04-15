#!/usr/bin/env python3
from random import sample


def random_insert(achievements):
    return (sample(achievements, 5))


def gen_player_achievements(achievements) -> set:
    return (set(random_insert(achievements)))


def analysis(players, achievements):
    print(f"\nCommon achievements: {set.intersection(*players.values())}\n")

    for player_name, player_set in players.items():
        excluding_player = set()
        for other_name, other_set in players.items():
            if other_name != player_name:
                excluding_player = excluding_player.union(other_set)
        unique = player_set - excluding_player
        print(f"Only {player_name} has: {unique}")
    print("\n")

    for missing_name, missing_set in players.items():
        all_achievements = set(achievements)
        missing = all_achievements - missing_set
        print(f"{missing_name} is missing: {missing}")


def main():
    print("=== Achievement tracker system ===")
    players = {
              "Alice": set(),
              "Bob": set(),
              "Charlie": set(),
              "Dylan": set()
              }

    achievements = [
                   "Crafting Genius",
                   "Strategist",
                   "World Savior",
                   "Speed Runner",
                   "Survivor",
                   "Master Explorer",
                   "Treasure Hunter",
                   "Unstoppable",
                   "First steps",
                   "Collector Supreme",
                   "Untouchable",
                   "Sharp Mind",
                   "Boss Slayer"
                   ]

    for player_name in players:
        players[player_name] = gen_player_achievements(achievements)
        print(f"Player {player_name}: {players[player_name]}")
    analysis(players, achievements)


main()
