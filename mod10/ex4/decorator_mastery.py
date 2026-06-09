#!/usr/bin/env python3
from collections.abc import Callable
from functools import wraps
from time import (sleep,
                  perf_counter)


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*pargs, **kwargs):
        print(f"Casting {func.__name__}...")
        start = perf_counter()
        result = func(*pargs, **kwargs)
        end = perf_counter()
        elapsed_time = end - start
        print(f"Spell completed in {round(elapsed_time, 3)} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power")

            if power is None:
                for arg in reversed(args):
                    if isinstance(arg, int):
                        power = arg
                        break

            if power is None or power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    else:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts"
                        )
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (len(name) >= 3 and
                all(c.isalpha() or
                    c.isspace() for c in name))

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def hollow_purple() -> str:
    sleep(0.101)
    return "Hollow purple cast!\nGet back in the lobby!"


@retry_spell(5)
def red() -> str:
    raise RuntimeError("Skill issue tbh")


@retry_spell(5)
def blue() -> str:
    return "Get back in the lobby!"


def main() -> None:
    test_powers = [5, 13, 5, 17]
    spell_names = ['tsunami', 'earthquake', 'blizzard', 'meteor']
    mage_names = ['Ember', 'Sage', 'Zara', 'Casey', 'Morgan', 'Rowan']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

    print("=== Spell Timer ===")
    spell = hollow_purple()
    print(f"Result: {spell}")

    print("\n=== Retrying Broken Spell ===")
    try:
        broken_spell = red()
        print(broken_spell)
    except RuntimeError as error_message:
        print(error_message)

    print("\n=== Retrying Valid Spell ===")
    valid_spell = blue()
    print(valid_spell)

    print("\n=== MageGuild ===")
    print("=== Valid Mage Name ===")
    guild = MageGuild()
    for name in mage_names:
        mage = guild.validate_mage_name(name)
        print(mage)
    print("\n=== Invalid Mage Name ===")
    for invalid_name in invalid_names:
        invalid_mage = guild.validate_mage_name(invalid_name)
        print(invalid_mage)
    print("\n=== Power Validation ===")
    for spell in spell_names:
        for power_level in test_powers:
            print(guild.cast_spell(spell, power=power_level))


if __name__ == "__main__":
    main()
