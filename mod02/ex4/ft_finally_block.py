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


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Caught PlantError: "
                         f"Invalid plant name to water: {plant_name}")


def test_watering_system(test_cases: list[str]) -> None:
    print("Opening watering system")
    try:
        for i in test_cases:
            water_plant(i)
    except (PlantError, AttributeError) as error_message:
        if isinstance(error_message, PlantError):
            print(error_message)
        elif isinstance(error_message, AttributeError):
            print(f"Caught AttributeError: {error_message}")
    finally:
        print("Closing watering system\n")
        # print("Cleanup always happens, even with errors!")


def main() -> None:
    valid_test = [
        ("Tomato"),
        ("Letuccee"),
        ("Carrot")
    ]
    invalid_test = [
        ("Tomato"),
        # (24),
        ("#carrot")
    ]
    print("=== Garden Watering System ===")
    print("Testing valid plants...")
    test_watering_system(valid_test)
    print("Testing invalid plants...")
    test_watering_system(invalid_test)
    print("Cleanup always happens, even with errors!")


main()
