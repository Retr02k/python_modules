#!/usr/bin/env python3

class Plant:
    def __init__(self, plant_name: str, plant_height: float, plant_days: int) -> None:
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_days = plant_days

    def show(self) -> None:
        print(f"{self.plant_name.capitalize()}: {self.plant_height}cm, "
              f"{self.plant_days} days old")


if __name__ == "__main__":
    plants = [
        ("rose", 25.0, 30),
        ("sunflower", 80.0, 45),
        ("cactus", 15.0, 120)
    ]

    print("=== Garden Plant Registry ===")
    objs = (Plant(*i) for i in plants)
    for flower in objs:
        flower.show()
