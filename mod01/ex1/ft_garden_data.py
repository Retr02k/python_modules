#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

def show(self):
      return f""

rose = Plant("rose", 25, 30)
sunflower = Plant("sunflower", 80, 45)
cactus = Plant("cactus", 15, 120)

print("=== Garden Plant Registry ===")
print(f"{rose.name.capitalize()}: {rose.height}cm, "
      f"{rose.age} days old")
print(f"{sunflower.name.capitalize()}: {sunflower.height}cm, "
      f"{sunflower.age} days old")
print(f"{cactus.name.capitalize()}: {cactus.height}cm, "
      f"{cactus.age} days old")
