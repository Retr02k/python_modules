#!/usr/bin/env python3
from ex4.ft_garden_security import GardenSec


class Flower(GardenSec):
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_days: int,
                 color: str
                 ) -> None:
        super().__init__(plant_name, plant_height, plant_days)
        self.color = color

    def bloom(self) -> None:
        if self.plant_days > 14:
            print(f"{self.plant_name.capitalize()} is blooming beautifully!\n")
        else:
            print(f"{self.plant_name.capitalize()} has not bloomed yet\n"
                  f"[asking the {self.plant_name} to bloom]\n")

    def show(self) -> None:
        print("=== Flower")
        print(f"{self.plant_name.capitalize()}: {self.plant_height:.1f}cm, "
              f"{self.plant_days} days old")
        print(f"Color: {self.color}")
        self.bloom()


class Tree(GardenSec):
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_days: int,
                 trunk_diameter: float
                 ) -> None:
        super().__init__(plant_name, plant_height, plant_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.plant_name} to produce shade]")
        if self.trunk_diameter < 10:
            print(f"{self.plant_name.capitalize()} produces very little shade,"
                  f" of {self.plant_height:.1f}cm long and "
                  f"{self.trunk_diameter:.1f}cm wide\n")
        elif 10 <= self.trunk_diameter <= 20:
            print(f"{self.plant_name.capitalize()} produces light, "
                  f"patchy shade of {self.plant_height:.1f}cm long and "
                  f"{self.trunk_diameter:.1f}cm wide\n")
        elif 20 < self.trunk_diameter <= 40:
            print(f"{self.plant_name.capitalize()} produces decent, "
                  f"noticeable shade of {self.plant_height:.1f}cm long and "
                  f"{self.trunk_diameter:.1f}cm wide\n")
        elif self.trunk_diameter > 40:
            print(f"{self.plant_name.capitalize()} produces strong, "
                  f"dense shade of {self.plant_height:.1f}cm long and "
                  f"{self.trunk_diameter:.1f}cm wide\n")

    def show(self) -> None:
        print("=== Tree")
        print(f"{self.plant_name.capitalize()}: {self.plant_height}cm, "
              f"{self.plant_days} days old")
        print(f"Trunk diameter: {self.trunk_diameter:.1f}")
        self.produce_shade()


class Vegetable(GardenSec):
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_days: int,
                 harvest_season: str,
                 nutritional_value: float,
                 growth_rate: float,
                 days_passed: int
                 ) -> None:
        super().__init__(plant_name, plant_height, plant_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        self.growth_rate = growth_rate
        self.days_passed = days_passed

    def grow(self) -> None:
        self.plant_height += self.growth_rate
        self.nutritional_value = (self.plant_height * self.growth_rate)

    def age(self) -> None:
        self.plant_days += 1

    def pass_days(self) -> None:
        print(f"\nMake {self.plant_name} grow and age "
              f"for {self.days_passed} days")
        for i in range(self.days_passed):
            self.age()
            self.grow()

    def show(self) -> None:
        print("=== Vegetable")
        print(f"{self.plant_name.capitalize()}: {self.plant_height:.1f}cm, "
              f"{self.plant_days} days old")
        print(f"Harvest season: {self.harvest_season.capitalize()}")
        print(f"Nutritional value: {self.nutritional_value}")
        self.pass_days()
        print(f"{self.plant_name.capitalize()}: {self.plant_height:.1f}cm, "
              f"{self.plant_days} days old")
        print(f"Harvest season: {self.harvest_season.capitalize()}")
        print(f"Nutritional value: {self.nutritional_value:.1f}")


if __name__ == "__main__":
    flowers = [
        ("rose", 15.0, 10, "red"),
        ("cactus", 30.0, 90, "green")
    ]

    trees = [
        ("oak", 200.0, 365, 5.0)
    ]

    vegetables = [
        ("tomato", 5.0, 10, "april", 0.0, 0.8, 20)
    ]

    flower = (Flower(*i) for i in flowers)
    tree = (Tree(*i) for i in trees)
    vegetable = (Vegetable(*i) for i in vegetables)

    for flower_item in flower:
        flower_item.show()
    for tree_item in tree:
        tree_item.show()
    for vegetable_item in vegetable:
        vegetable_item.show()
