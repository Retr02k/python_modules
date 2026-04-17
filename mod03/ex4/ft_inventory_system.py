#!/usr/bin/env python3
import sys


def parsing(arguments: list[str]) -> dict[str, int]:
    inventory = {}

    for arg in arguments:
        if arg.count(":") != 1:
            print(f"Invalid syntax: {arg}")
            continue
        item_name, item_value = arg.split(':')
        if not item_name or not item_value:
            print(f"Invalid parameter: {arg}")
            continue
        if item_name in inventory:
            print(f"Redundant item: {item_name} - discarding...")
            continue
        try:
            value = int(item_value)
        except ValueError as error_message:
            print(f"Quantity error for {item_name}: {error_message}")
            continue
        inventory[item_name] = value
    print(f"Got inventory: {inventory}")
    print(f"Item list: {inventory.keys()}")
    return inventory


def analysis(inventory: dict[str, int]) -> None:
    item_count = len(inventory.keys())
    quantity_count = sum(inventory.values())
    percentage_list = {}
    print(f"Total quantity of the {item_count} items: {quantity_count}")
    for item in inventory:
        item_percentage = ((inventory[item] / quantity_count) * 100)
        percentage_list[item] = inventory[item]
        print(f"Item {item} represents {round(item_percentage, 1)}%")

    percentage_list = inventory.items()
    max_value = max(inventory.values())
    min_value = min(inventory.values())
    for key, value in percentage_list:
        if inventory[key] == max_value:
            print(f"Item most abundant: {key} with quantity {max_value}")
        elif inventory[key] == min_value:
            print(f"Item least abundant: {key} with quantity {min_value}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parsing(sys.argv[1:])
    analysis(inventory)


if __name__ == "__main__":
    main()
