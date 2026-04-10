#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, error_message: str = "Unknown plant error") -> None:
        self.error_message: str = error_message
        super().__init__(self.error_message)

    def __str__(self) -> str:
        return self.error_message


class PlantError(GardenError):
    def __init__(self, error_message: str = "Unknown plant error") -> None:
        super().__init__(error_message)


class WaterError(GardenError):
    def __init__(self, error_message: str = "Unknown watering error") -> None:
        super().__init__(error_message)


print("=== Custom Garden Errors Demo ===")

print("\nTesting PlantError...")
try:
    raise PlantError("The tomato plant is wilting!")
except PlantError as error_message:
    print(f"Caught PlantError: {error_message}\n")

print("Testing WaterError...")
try:
    raise WaterError("Not enough water in the tank!")
except WaterError as error_message:
    print(f"Caught WaterError: {error_message}\n")

print("Testing catching all garden errors...")
try:
    raise PlantError
except GardenError as error_message:
    print(f"Caught GardenError: {error_message}")

try:
    raise WaterError
except GardenError as error_message:
    print(f"Caught GardenError: {error_message}\n")

print("All custom error types work correctly!")
