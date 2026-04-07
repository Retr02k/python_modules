#!/usr/bin/env python3.14

if __name__ == "__main__":
    def input_temperature(temp_str: str) -> int:
        return (int(temp_str))

    def test_temperature(func, value) -> None:
        print("=== Garden Temperature ===")
        try:
            print(f"Input data is '{value}'")
            print(f"Temperature is now {func(value)}°C")
        except ValueError as error_message:
            print(error_message)

test_temperature(input_temperature, "25")
test_temperature(input_temperature, "abc")
