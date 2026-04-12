#!/usr/bin/env python3
import sys


print("=== Player Score Analytics ===")
arg_count: int = len(sys.argv)
if arg_count <= 1:
    print("No scores provided. Usage: python3 "
          "ft_score_analytics.py <score1> <score2> ...")
else:
    new_list: list[int] = []
    try:
        for i in range(1, arg_count):
            try:
                new_list.append(int(sys.argv[i]))
            except ValueError:
                print(f"Invalid parameter: '{sys.argv[i]}")
                continue
        if not new_list:
            print("No scored provided. Usage: python3 "
                  "ft_score_analytics.py <score1> <score2> ...")
        else:
            print(f"Scores processed: {new_list}")
            print(f"Total players: {len(new_list)}")
            print(f"Total score: {sum(new_list)}")
            print(f"Average score: {sum(new_list) / len(new_list)}")
            print(f"High score: {max(new_list)}")
            print(f"Low score: {min(new_list)}")
            print(f"Score range: {max(new_list) - min(new_list)}")
    except ValueError:
        print(f"Invalid parameter: {sys.argv[i]}")
