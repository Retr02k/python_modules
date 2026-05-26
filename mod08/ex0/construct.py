#!/usr/bin/env python3
import sys
import os
import site


def is_virtual_environment() -> bool:
    return (
        hasattr(sys, "real_prefix")
        or sys.prefix != sys.base_prefix
    )


def get_venv_name() -> str:
    return os.path.basename(sys.prefix)


def get_site_packages() -> str:
    paths: list[str] = site.getsitepackages()

    if paths:
        return paths[0]

    return "Unknown"


def main() -> None:
    python_path: str = sys.executable

    if is_virtual_environment():
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {python_path}")
        print(f"Virtual Environment: {get_venv_name()}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(get_site_packages())

    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {python_path}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
