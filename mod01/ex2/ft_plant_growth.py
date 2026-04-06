#!/usr/bin/env python3
from ex1.ft_garden_data import Plant


class GrowthPlant(Plant):
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_days: int,
                 growth_rate: float
                 ):
        super().__init__(plant_name, plant_height, plant_days)
        self.growth_rate = growth_rate

    def grow(self):
        self.plant_height += self.growth_rate
        return self.plant_height

    def age(self):
        self.plant_days += 1
        return self.plant_days

    def pass_one_day(self):
        self.grow()
        self.age()

    def show(self):
        print(f"{self.plant_name.capitalize()}: {self.plant_height:.1f}cm, "
              f"{self.plant_days} days old")


if __name__ == "__main__":
    rose = GrowthPlant("rose", 25, 30, 0.8)
    print("=== Garden Plant Growth ===")
    intial_height = rose.plant_height

    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.show()
        rose.pass_one_day()
    weekly_growth = rose.plant_height - intial_height
    print(f"Growth this week: +{weekly_growth:.1f}cm")
