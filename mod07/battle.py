#!/usr/bin/env python3
from ex0 import FlameFactory, AquaFactory


if __name__ == "__main__":
    def function(factory_object):
        try:
            base = factory_object.create_base()
            evolved = factory_object.create_evolved()
            print(base.describe())
            print(base.attack())
            print(evolved.describe())
            print(evolved.attack())
        except Exception as error_message:
            print(error_message)

    def battle(factory_a, factory_b):
        gabriel = factory_a.create_base()
        diogo = factory_b.create_base()
        print(gabriel.describe())
        print("vs")
        print(diogo.describe())
        print(gabriel.attack())
        print(diogo.attack())

    print("Testing factory")
    gabriel = FlameFactory()
    function(gabriel)
    print("\nTesting factory")
    diogo = AquaFactory()
    function(diogo)
    print("\nTesting Battle")
    battle(gabriel, diogo)
