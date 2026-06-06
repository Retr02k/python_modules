#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    ctd = 0

    def counter() -> int:
        nonlocal ctd
        ctd += 1
        return ctd
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def acumulator(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power
    return acumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchant(enchantment_item: str) -> str:
        return f"{enchantment_type} {enchantment_item}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any | str:
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    initial_powers = [52, 26, 27]
    power_additions = [15, 13, 17, 8, 8]
    enchantment_types = ['Earthen', 'Flowing', 'Shocking']
    items_to_enchant = ['Cloak', 'Amulet', 'Armor', 'Sword']

    try:
        print("=== mage_counter ===")
        counter = mage_counter()

        for _ in range(5):
            print(counter())

        print("\n=== spell_accumulator ===")
        initial_powers = [52, 26, 27]
        power_additions = [15, 13, 17, 8, 8]

        for initial_power in initial_powers:
            accumulator = spell_accumulator(initial_power)
            print(f"\nStarting power: {initial_power}")

            for amount in power_additions:
                print(f"+{amount} -> {accumulator(amount)}")

        print("\n=== enchantment_factory ===")
        enchantment_types = ["Earthen", "Flowing", "Shocking"]
        items_to_enchant = ["Cloak", "Amulet", "Armor", "Sword"]

        for enchantment_type in enchantment_types:
            enchant = enchantment_factory(enchantment_type)

            for item in items_to_enchant:
                print(enchant(item))

        print("\n=== memory_vault ===")
        vault = memory_vault()

        vault["store"]("power", 52)
        vault["store"]("enchantment", "Earthen")
        vault["store"]("item", "Cloak")

        print(vault["recall"]("power"))
        print(vault["recall"]("enchantment"))
        print(vault["recall"]("item"))
        print(vault["recall"]("missing"))
    except Exception as error_message:
        print(error_message)


if __name__ == "__main__":
    main()
