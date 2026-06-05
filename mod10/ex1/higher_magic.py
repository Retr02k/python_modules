#!/usr/bin/env python3
from collections.abc import Callable


def divergent_fist(target: str, power: int) -> str:
    return (f"Divergent Fist strikes {target} with delayed impact for"
            f" {power} damage")


def black_flash(target: str, power: int) -> str:
    return (f"Black Flash distorts space on {target} for"
            f" {power} cursed energy damage")


def hollow_purple(target: str, power: int) -> str:
    return f"Hollow Purple erases {target} from existence for {power} damage"


def domain_expansion(target: str, power: int) -> str:
    return (f"Domain Expansion traps {target} in guaranteed hit territory for"
            f" {power} damage")


def red(target: str, power: int) -> str:
    return (f"Reversal Red repels {target} with positive cursed energy for"
            f" {power} damage")


def blue(target: str, power: int) -> str:
    return (f"Amplification Blue pulls {target} into negative cursed energy "
            f"for {power} damage")


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: (spell(target, power) if
                                  condition(target, power) else
                                  "Spell fizzled")


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [spell(target, power) for spell in spells]


def main() -> None:
    targets = [
        'Sukuna',
        'Gojo',
        'Mahito',
        'Jogo',
        'Hanami',
        'Choso',
        'Toji'
    ]

    spell_powers = [
        150,
        200,
        75,
        120,
        90,
        110,
        180
    ]

    spell_list = [
        divergent_fist,
        black_flash,
        hollow_purple,
        domain_expansion,
        red,
        blue
    ]

    for target, power in zip(targets, spell_powers):
        # Combined Spell
        combined = spell_combiner(blue, red)
        print(f"First Spell:\n{combined('Sukuna', 100)[0]}")
        print(f"\nSecond spell:\n{combined('Sukuna', 100)[1]}")
        print(f"\nCombined Spell\n{combined('sukuna', 100)}")

        # Amplified Spell
        amplified = power_amplifier(domain_expansion, 2)
        print(f"\nAmplified spell:\n{amplified('Jogo', 100)}")

        # Conditional Spell
        conditional = conditional_caster(lambda t, p: p > 70, black_flash)
        print(f"\nValid Conditional Spell:\n{conditional('Mahito', 100)}")
        print(f"\nInvalid Conditional Spell:\n{conditional('Mahito', 10)}")

        # Sequence Spell
        sequence = spell_sequence(spell_list)
        print(f"\n{sequence('Hanami', 50)}")


if __name__ == "__main__":
    main()
