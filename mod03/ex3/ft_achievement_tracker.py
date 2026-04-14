#!/usr/bin/env python3
from random import sample, choice


def random_insert(achievements):
    return(sample(achievements, 5))


def gen_player_achievements(achievements) -> type[set]:
    return (set(random_insert(achievements)))

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
main()
