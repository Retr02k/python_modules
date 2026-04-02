#!/usr/bin/env python3
from ex1.ft_garden_data import Plant


class GardenSec(Plant):
    def __init__(self, plant_name: str, plant_height: float, plant_days: int):
        super().__init__(plant_name, plant_height, plant_days)

    _validate_ = {"plant_height", "plant_days"}

    def __setattr__(self, name, value):
        if name in self._validate_ and value <= 0:
            raise ValueError(f"{self.plant_name}: Error: "
                             f"{name} can't be negative")
        super().__setattr__(name, value)


if __name__ == "__main__":
    flowers = [
        ("rose", 15, 10),
        ("cactus", 30, 40),
        ("sunflower", 100, 35)
    ]

    attempt_list = [
        ("plant_height", 25, "Height updated: {}cm",
         "Height update rejected!"),
        ("plant_days", 30, "Age updated: {} days",
         "Age update rejected!"),
    ]

    print("=== Garden Security System ===")
    obj = [GardenSec(*i) for i in flowers]

    for plant in obj:
        print(
            f"Plant created: {plant.plant_name.capitalize()}: "
            f"{plant.plant_height:.1f}cm, {plant.plant_days} days old"
        )

        for attr_name, value, succ_text, rej_text in attempt_list:
            try:
                setattr(plant, attr_name, value)
                print(succ_text.format(value))
            except ValueError as err:
                print(err)
                print(rej_text)

        print(
            f"Current state: {plant.plant_name.capitalize()}: "
            f"{plant.plant_height:.1f}cm, {plant.plant_days} days old\n"
        )
