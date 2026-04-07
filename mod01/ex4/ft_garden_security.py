#!/usr/bin/env python3
from ex1.ft_garden_data import Plant


class GardenSec(Plant):
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_days: int
                 ) -> None:
        super().__init__(plant_name, plant_height, plant_days)
        self._plant_height = plant_height
        self._plant_days = plant_days

    def get_height(self) -> float:
        return self._plant_height

    def set_height(self, new_value: float) -> None:
        if new_value <= 0:
            raise ValueError(f"{self.plant_name}: Error, height "
                             f"can't be negative\nHeight update rejected")
        self._plant_height = new_value

    def get_age(self) -> int:
        return self._plant_days

    def set_age(self, new_value: int) -> None:
        if new_value <= 0:
            raise ValueError(f"{self.plant_name}: Error, age "
                             f"can't be negative\nAge update rejected")
        self._plant_days = new_value

    def show(self) -> None:
        print(f"Plant created: {self.plant_name.capitalize()}: "
              f"{self._plant_height}cm, {self._plant_days} days old")


if __name__ == "__main__":
    flowers = [
        ("rose", 15, 30),
        ("cactus", 30, 40),
        ("sunflower", 50.5, 25)
    ]

    attempt_list = [
        ("set_height", -40, "Height updated: {}cm"),
        ("set_age", -30, "Age updated: {} days")
    ]

    obj = [GardenSec(*i) for i in flowers]
    print("=== Garden Security System ===")
    for flower_item in obj:
        flower_item.show()
        for method_name, value, succ_text in attempt_list:
            try:
                method = getattr(flower_item, method_name)
                method(value)
                print(succ_text.format(value))
            except ValueError as error_message:
                print(error_message)

        print(
            f"Current state: {flower_item.plant_name.capitalize()}: "
            f"{flower_item.get_height()}cm, {flower_item.get_age()} days old\n"
        )
