#!/usr/bin/env python3
from ex1.ft_garden_data import Plant


class GrowthPlant(Plant):
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_days: int,
                 growth_rate: float
                 ) -> None:
        super().__init__(plant_name, plant_height, plant_days)
        self.growth_rate = growth_rate

    def grow(self) -> float:
        self.plant_height += self.growth_rate
        return self.plant_height

    def age(self) -> int:
        self.plant_days += 1
        return self.plant_days

    def pass_one_day(self) -> None:
        self.grow()
        self.age()

    def show(self) -> None:
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            print(f"{self.plant_name.capitalize()}: "
                  f"{self.plant_height:.1f}cm, "
                  f"{self.plant_days} days old")
            self.pass_one_day()


if __name__ == "__main__":
    rose = GrowthPlant("rose", 25, 30, 0.8)
    print("=== Garden Plant Growth ===")
    initial_height = rose.plant_height
    rose.show()
    weekly_growth = rose.plant_height - initial_height
    print(f"Growth this week: +{weekly_growth:.1f}cm")
