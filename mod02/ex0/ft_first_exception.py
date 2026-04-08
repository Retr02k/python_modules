#!/usr/bin/env python3.14
def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature(func, value) -> None:
    print("=== Garden Temperature ===")
    try:
        print(f"Input data is '{value}'")
        print(f"Temperature is now {func(value)}°C")
    except ValueError as error_message:
        print(error_message)


if __name__ == "__main__":
    test_temperature(input_temperature, "25")
    test_temperature(input_temperature, "5")
    test_temperature(input_temperature, "33")
    test_temperature(input_temperature, "42")
    test_temperature(input_temperature, "abc")
    test_temperature(input_temperature, "tres")

    print("\nAll tests completed - program didn't crash!")
