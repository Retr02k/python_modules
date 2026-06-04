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

artifact_sorter = lambda artifacts: sorted(artifacts, key=lambda a: a['power'], reverse=True)
power_filter = lambda mages, min_power: list(filter(lambda mage: mage['power'] >= min_power, mages))
spell_transformer = lambda spells: list(map(lambda spell: '* ' + spell + ' *', spells))
mage_stats = lambda mages: {
    'Most powerful mage': max(mages, key=lambda a: a['power'])['power'],
    'Least powerful mage': min(mages, key=lambda a: a['power'])['power'],
    'Avreage power level': round(sum(mage['power'] for mage in mages) / len(mages), 2)
}
print(f"Artifact Sorter:\n{artifact_sorter(artifacts)}")
print(f"\nPower Filter:\n{power_filter(mages, 70)}")
print(f"\nSpell Transformer:\n{spell_transformer(spells)}")
print(f"\nMage Stats:\n{mage_stats(mages)}")