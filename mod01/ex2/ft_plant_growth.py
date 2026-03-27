#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 6

    def days(self):
        self.age += 6

    def get_info(self):
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age} days old")


print("=== Day 1 ===")
rose = Plant("rose", 25, 30)
rose.get_info()
print("=== Day 7 ===")
rose.grow()
rose.days()
rose.get_info()
print("Growth this week: +6cm")
