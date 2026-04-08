#!/usr/bin/env python3
from ex0.ft_first_exception import test_temperature


def input_temperature(temp_str: str) -> int:
    int_temp = int(temp_str)
    if int_temp < 0:
        raise ValueError(f"{temp_str}°C is too cold for plants (min 0°C)")
    elif int_temp > 40:
        raise ValueError(f"{temp_str}°C is too hot for plants (max 40°C)")
    return int_temp


if __name__ == "__main__":
    test_temperature(input_temperature, "25")
    test_temperature(input_temperature, "abc")
    test_temperature(input_temperature, "100")
    test_temperature(input_temperature, "-50")

    print("\nAll tests completed - program didn't crash!")
