import alchemy

try:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing {alchemy.create_air.__name__}: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print(alchemy.create_earth())
except AttributeError as error_message:
    print(error_message)
