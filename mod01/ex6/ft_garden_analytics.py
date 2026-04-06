#!/usr/bin/env python3


class Plant:
    class Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(f"Stats: {self.grow_calls} grow, {self.age_calls} age, "
                  f"{self.show_calls} show")

    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_days: int,
                 growth_rate: float = 0.0
                 ):
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_days = plant_days
        self.growth_rate = growth_rate
        self._stats = Plant.Stats()

    def grow(self):
        self._stats.grow_calls += 1
        self.plant_height += self.growth_rate

    def age(self):
        self._stats.age_calls += 1
        self.plant_days += 10

    def print_info(self):
        print(f"{self.plant_name.capitalize()}: {self.plant_height:.1f}cm, "
              f"{self.plant_days} days old")

    def show(self):
        self._stats.show_calls += 1
        self.print_info()

    @classmethod
    def placeholder(cls, plant_name):
        return cls(plant_name, 0.0, 0, 0.0)

    @staticmethod
    def is_year_old(age):
        return f"Is {age} days more than a year? -> {age > 365}"


class Flower(Plant):
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_days: int,
                 color: str,
                 growth_rate: float = 0.0
                 ):
        super().__init__(plant_name,
                         plant_height,
                         plant_days,
                         growth_rate
                         )
        self.color = color

    def bloom(self):
        if self._stats.age_calls > 0:
            print(f"{self.plant_name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.plant_name.capitalize()} has not bloomed yet")

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        self.bloom()


class Seed(Flower):
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_days: int,
                 color: str,
                 growth_rate: float = 0.0
                 ):
        super().__init__(plant_name,
                         plant_height,
                         plant_days,
                         color,
                         growth_rate
                         )
        self.seeds = 0

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")
        print("[make sunflower grow, age and bloom]")
        self.grow()
        self.age()
        if self._stats.age_calls > 0:
            self.seeds = 42
        self.print_info()
        self.bloom()
        print(f"Seeds: {self.seeds}")
        display_stats(self)


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self.shade_calls = 0

        def display(self):
            print(f"Stats: {self.grow_calls} grow, {self.age_calls} age, "
                  f"{self.show_calls} show, {self.shade_calls} shade")

    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_days: int,
                 trunk_diameter: float,
                 growth_rate: float = 0.0
                 ):
        super().__init__(plant_name, plant_height, plant_days, growth_rate)
        self.trunk_diameter = trunk_diameter
        self._stats = Tree.Stats()

    def produce_shade(self):
        self._stats.shade_calls += 1
        print(f"Tree {self.plant_name.capitalize()} now produces a shade of "
              f"{self.plant_height:.1f}cm long "
              f"and {self.trunk_diameter:.1f}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")
        display_stats(self)
        print("[asking the oak to produce shade]")
        self.produce_shade()
        display_stats(self)


def display_stats(plant):
    print(f"[statistics for {plant.plant_name.capitalize()}]")
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(Plant.is_year_old(30))
    print(f"{Plant.is_year_old(400)}\n")

    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red", 8)
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.age()
    rose.show()
    display_stats(rose)

    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()

    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow", 30.0)
    sunflower.show()

    print("=== Anonymous")
    unknown = Plant.placeholder("Unknown plant")
    unknown.show()
    display_stats(unknown)
