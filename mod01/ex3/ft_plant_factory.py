#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


plants = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
    ]
obj = []

print("=== Plant Factory Output ===")
for x in plants:
    name, height, age = x
    plant = Plant(name, height, age)
    obj.append(plant)
    print(f"Created: {plant.name} ({plant.height}cm, "
          f"{plant.age} days)")
print("\nTotal plants created: 5")
