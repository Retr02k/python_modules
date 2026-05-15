from alchemy.elements import create_air, create_earth
from ..potions import strength_potion
from elements import create_fire

def lead_to_gold() -> str:
    return (f"Recipe transmutating Lead to Gold: "
            f"brew {create_air()} and {strength_potion()} "
            f"mixed with {create_fire()}")
