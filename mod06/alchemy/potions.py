import alchemy.elements
from elements import create_water, create_fire

def healing_potion() -> str:
    return (f"Healing potion brewed with "
            f"{alchemy.elements.create_earth()} and "
            f"{alchemy.elements.create_air()}")

def strength_potion() -> str:
    return (f"Strength potion brewed with "
            f"{create_fire()} and "
            f"{create_water()}")
