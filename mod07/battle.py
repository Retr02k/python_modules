#!/usr/bin/env python3
from ex0 import FlameFactory, AquaFactory


if __name__ == "__main__":
    def function(factory_object):
        base = factory_object.create_base()
        evolved = factory_object.create_evolved()
        print(base.describe())
        print(base.attack())
        print(evolved.describe())
        print(evolved.attack())

    def battle(factory_a, factory_b):
        creature_a = factory_a.create_base()
        creature_b = factory_b.create_base()
        print(creature_a.describe())
        print(" VS")
        print(creature_b.describe())
        print(" FIGHT!")
        print(creature_a.attack())
        print(creature_b.attack())

    print("Testing factory")
    flame_factory = FlameFactory()
    function(flame_factory)
    print("\nTesting factory")
    aqua_factory = AquaFactory()
    function(aqua_factory)
    print("\nTesting Battle")
    battle(flame_factory, aqua_factory)
