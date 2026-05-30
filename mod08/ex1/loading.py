#!/usr/bin/env python3

import importlib
import sys
from types import ModuleType


def check_dependencies() -> dict[str, ModuleType]:
    packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }

    loaded_modules = {}

    print("Checking dependencies:")

    for package, message in packages.items():
        try:
            module = importlib.import_module(package)

            print(
                f"[OK] {package} ({module.__version__})"
                f" - {message}"
            )

            loaded_modules[package] = module

        except ImportError:
            print(f"[KO] {package} not installed")

    return loaded_modules


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")

    modules = check_dependencies()

    required = ["pandas", "numpy", "matplotlib"]

    for package in required:
        if package not in modules:
            print("\nInstall required dependencies first.")
            sys.exit(1)

    pandas = modules["pandas"]
    numpy = modules["numpy"]

    matplotlib = importlib.import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")

    matrix = numpy.sort(
        numpy.random.rand(1000)
    )

    dataframe = pandas.DataFrame(
        matrix,
        columns=["values"]
    )

    print(f"Processing {len(dataframe)} data points...")

    print("Generating visualization...")

    matplotlib.plot(dataframe["values"])

    matplotlib.title("Matrix Data Analysis")
    matplotlib.xlabel("Index")
    matplotlib.ylabel("Value")

    matplotlib.savefig("matrix_analysis.png")

    matplotlib.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
