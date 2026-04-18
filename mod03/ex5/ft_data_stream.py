#!/usr/bin/env python3
from random import choice
from typing import Generator


def gen_event(
    players: list[str], actions: list[str]
) -> Generator[tuple[str, str], None, None]:
    while True:
        yield (choice(players), choice(actions))


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while events:
        event = choice(events)
        events.remove(event)
        yield event


if __name__ == "__main__":
    def main() -> None:
        events: list[tuple[str, str]] = []
        print("=== Game Data Stream Processor ===")
        players = [
                  "Alice",
                  "Bob",
                  "Charlie",
                  "Dylan"
                  ]

        actions = [
                  "run",
                  "eat",
                  "sleep",
                  "grab",
                  "move",
                  "climb",
                  "swim",
                  "release",
                  "use",
                  ]

        gen = gen_event(players, actions)
        for i in range(0, 1010):
            event = next(gen)
            if i < 1000:
                print(f"Event {i}: Player {event[0]} "
                      f"did action {event[1]}")
            else:
                events.append(event)

        print(f"Built list of 10 events: {events}")
        for event in consume_event(events):
            print(f"Got event from list: {event}")
            print(f"Remains in list: {events}")

    main()
