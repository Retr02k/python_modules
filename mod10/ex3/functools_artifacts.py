#!/usr/bin/env python3
from typing import Any
from collections.abc import Callable
from functools import (
    reduce,
    partial,
    lru_cache,
    singledispatch
)
from operator import (
    add,
    mul
)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} got hit by an {element} attack with {power} ATK"


def spell_reducer(spells: list[int], operation: str) -> int:
    operations_list: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    if not spells:
        return 0
    elif operation not in operations_list:
        raise ValueError(
            f"Unknown operation '{operation}'. "
            "Supported operations: add, multiply, max, min"
        )
    return reduce(operations_list[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    elements = ["fire", "water", "earth", "wind"]

    return {
        element: partial(base_enchantment, 50, element)
        for element in elements
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be integer")

    if n < 0:
        raise ValueError("n must be non-negative")

    if n < 2:
        return n

    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def cast(spell: Any) -> str:
        return f"Unknown spell type: {spell}"

    @cast.register
    def _(spell: int) -> str:
        return f"Damage spell deals {spell} damage"

    @cast.register
    def _(spell: str) -> str:
        return f"Enchantment cast: {spell}"

    @cast.register
    def _(spell: list) -> str:
        return f"Multi-cast spell with {len(spell)} spells"

    return cast


def main() -> None:
    spell_powers = [13, 14, 35, 42, 16, 44]
    operations = ['add', 'multiply', 'max', 'min', 'unknown']
    fibonacci_tests = [13, 8, 19]

    print("=== Spell Reducer ===")
    for operation in operations:
        try:
            reducer = spell_reducer(spell_powers, operation)

            print(f"{operation}: {reducer}")

        except ValueError as error_message:
            print(error_message)

    print("\n=== Partial Enchanter ===")
    try:
        spells = partial_enchanter(base_enchantment)

        print(spells["fire"]("Zuko"))
        print(spells["water"]("Zuko"))
        print(spells["earth"]("Zuko"))
        print(spells["wind"]("Zuko"))

    except Exception as error_message:
        print(error_message)

    print("\n=== Memoized Fibonacci ===")
    for number in fibonacci_tests:
        try:
            print(f"fib({number}) = {memoized_fibonacci(number)}\n"
                  f"{memoized_fibonacci.cache_info()}\n")

        except (ValueError, TypeError) as error_message:
            print(error_message)

    print("\n=== Spell Dispatcher ===")
    spell = spell_dispatcher()

    try:
        print(spell(42))
        print(spell("fireball"))
        print(spell(spell_powers))
        print(spell({"gabriel": 5000}))
    except Exception as error_message:
        print(error_message)


if __name__ == "__main__":
    main()
