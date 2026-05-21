#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0.creatures import Flameling
from ex1.creatures import Sproutling

if __name__ == "__main__":
    def main() -> None:
        criatura_de_deus = Sproutling()
        gabriel = HealingCreatureFactory()
        base = gabriel.create_base()
        evolved = gabriel.create_evolved()
        print("Testing Creature with healing capability")
        print(" base:")
        print(base.describe())
        print(base.attack())
        print(base.heal(base))
        print(" evolved:")
        print(evolved.describe())
        print(evolved.attack())
        print(evolved.heal(evolved))

        print("\nTesting Creature with transform capability")
        diogo = TransformCreatureFactory()
        base = diogo.create_base()
        evolved = diogo.create_evolved()
        print(" base:")
        print(base.describe())
        print(base.attack())
        print(base.transform())
        print(base.attack())
        print(base.revert())
        print(" evolved:")
        print(evolved.describe())
        print(evolved.attack())
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())

    try:
        main()
    except Exception as error_message:
        print(error_message)