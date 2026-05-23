#!/usr/bin/env python3
import os
import sys


if __name__ == "__main__":
    def main() -> None:
        if 'VIRTUAL_ENV' in os.environ:
            print("\nMATRIX STATUS: Welcome to the construct\n")
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {sys.prefix}")
            print(f"Environment Path: {sys.prefix}\n")
            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting the global system.")
            print(f"Package installation path:\n{}")
        else:
            print("\nMATRIX STATUS: Your're still plugged in\n")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected\n")
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.\n")
            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env\Scripts\activate # On Windows\n")
            print("Then run this program again.")


    main()
