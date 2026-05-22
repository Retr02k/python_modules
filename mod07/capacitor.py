#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory

if __name__ == "__main__":
    def main() -> None:
        heal_factory = HealingCreatureFactory()
        heal_factory_base = heal_factory.create_base()
        heal_factory_evolved = heal_factory.create_evolved()
        print("Testing Creature with healing capability")
        print(" BASE:")
        print(heal_factory_base.describe())
        print(heal_factory_base.attack())
        print(heal_factory_base.heal())
        print(" EVOLVED:")
        print(heal_factory_evolved.describe())
        print(heal_factory_evolved.attack())
        print(heal_factory_evolved.heal())

        print("\nTesting Creature with transform capability")
        transform_factory = TransformCreatureFactory()
        transform_factory_base = transform_factory.create_base()
        transform_factory_evolved = transform_factory.create_evolved()
        print(" BASE:")
        print(transform_factory_base.describe())
        print(transform_factory_base.attack())
        print(transform_factory_base.transform())
        print(transform_factory_base.attack())
        print(transform_factory_base.revert())
        print(" EVOLVED:")
        print(transform_factory_evolved.describe())
        print(transform_factory_evolved.attack())
        print(transform_factory_evolved.transform())
        print(transform_factory_evolved.attack())
        print(transform_factory_evolved.revert())

    try:
        main()
    except ValueError as error_message:
        print(error_message)
