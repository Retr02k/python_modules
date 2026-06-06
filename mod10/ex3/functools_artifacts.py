#!/usr/bin/env python3
from collections.abc import Callable
from functools import (
    reduce,
    partial
)
from operator import (
    add,
    mul
)


def base_enchantment(power: int, element: str, target: str) -> str:
    elements = [
        "fire",
        "water",
        "earth",
        "wind"
    ]
    if element not in elements:
        raise ValueError(
            f"Unknown element '{element}'. "
            "supported elements: fire, water, earth, wind")
    return f"{target} got hit by an {element} attack with {power} ATK"


def spell_reducer(spells: list[int], operation: str) -> int:
    operations_list = {
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

#def memoized_fibonacci(n: int) -> int:


#def spell_dispatcher() -> Callable[[Any], str]:



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

if __name__ == "__main__":
    main()