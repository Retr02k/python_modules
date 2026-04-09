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


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("All custom error types work correctly!")
