#!/usr/bin/env python3
from random import randint


if __name__ == "__main__":
    def main() -> None:
        print("=== Game Data Alchemist ===")

        players = [
                  "Alice",
                  "bob",
                  "Charlie",
                  "dylan",
                  "Emma",
                  "Gregory",
                  "john",
                  "kevin",
                  "Liam"
                  ]

        all_players_cap = [
                          player.capitalize()
                          for player in players
                          ]
        only_cap_players = [
                           player
                           for player in players
                           if player == player.capitalize()
                           ]
        score = {
                player: randint(20, 100)
                for player in all_players_cap
                }
        average_score = (sum(score.values()) / len(score))
        high_scores = {
                      player: score[player]
                      for player in score
                      if score[player] > average_score
                      }
        print(f"Initial list of players: {players}")
        print(f"New list with all names capitalized: {all_players_cap}")
        print(f"New list of capitalized names only: {only_cap_players}")
        print(f"Score dict: {score}")
        print(f"Score average is {round(average_score, 2)}")
        print(f"High scores: {high_scores}")

    main()
