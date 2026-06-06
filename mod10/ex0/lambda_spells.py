#!/usr/bin/env python3


artifacts = [
    {'name': 'Earth Shield', 'power': 73, 'type': 'armor'},
    {'name': 'Earth Shield', 'power': 76, 'type': 'relic'},
    {'name': 'Fire Staff', 'power': 80, 'type': 'accessory'},
    {'name': 'Ice Wand', 'power': 106, 'type': 'accessory'}
    ]
mages = [
    {'name': 'Phoenix', 'power': 92, 'element': 'wind'},
    {'name': 'Rowan', 'power': 93, 'element': 'shadow'},
    {'name': 'Morgan', 'power': 96, 'element': 'water'},
    {'name': 'Phoenix', 'power': 67, 'element': 'earth'},
    {'name': 'Luna', 'power': 58, 'element': 'light'}
    ]
spells = ['darkness', 'lightning', 'tornado', 'freeze']


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: '* ' + spell + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda a: a['power'])['power'],
        'min_power': min(mages, key=lambda a: a['power'])['power'],
        'avg_power': round(
            sum(m['power'] for m in mages) / len(mages), 2
        )
    }


def main() -> None:
    print(f"Artifact Sorter:\n{artifact_sorter(artifacts)}")
    print(f"\nPower Filter:\n{power_filter(mages, 70)}")
    print(f"\nSpell Transformer:\n{spell_transformer(spells)}")
    print(f"\nMage Stats:\n{mage_stats(mages)}")


if __name__ == "__main__":
    main()
