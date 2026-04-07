#!/usr/bin/env python3
from ex1.ft_garden_data import Plant


if __name__ == "__main__":
    plants = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
        ]

    print("=== Plant Factory Output ===")
    obj = [Plant(*i) for i in plants]
    for plant in obj:
        print(f"{plant.plant_name.capitalize()}: {plant.plant_height:.1f}cm, "
              f"{plant.plant_days} days old")
    print(f"\nTotal plants created: {len(obj)}")
