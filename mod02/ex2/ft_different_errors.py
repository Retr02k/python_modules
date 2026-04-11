#!/usr/bin/env python3


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("ola.txt")
    elif operation_number == 3:
        "ola" + 42
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    error_list: list[tuple[type[Exception], int]] = [
        (ValueError, 0),
        (ZeroDivisionError, 1),
        (FileNotFoundError, 2),
        (TypeError, 3)
    ]
    for error_type, test in error_list:
        print(f"Testing operation {test}...")
        try:
            garden_operations(test)
        except error_type as error_message:
            print(f"Caught {error_type.__name__}: {error_message}\n")

    print("All error types tested successfully!")


test_error_types()
