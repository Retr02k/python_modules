from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability

class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self):
        return f"{self.name} uses Vine Whip!"
    
    def heal(self, target):
        if target is None:
            raise ValueError("Needs target creature")
        elif not isinstance(target, Creature):
            raise ValueError(f"{target} is not a Creature")
        elif target is self:
            return f"{self.name} heals itself for a small amount"
        else:
            return f"{self.name} heals {target.name} for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self):
        return f"{self.name} uses Petal Dance!"
    
    def heal(self, target):
        if target is None:
            raise ValueError("Needs target creature")
        elif not isinstance(target, Creature):
            raise ValueError(f"{target} is not a Creature")
        elif target is self:
            return f"{self.name} heals itself for a small amount"
        else:
            return f"{self.name} heals {target.name} for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        TransformCapability.__init__(self)
        Creature.__init__(self, "Shiftling", "Normal")

    def attack(self):
        if self.transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"
    
    def transform(self):
        if self.transformed is True:
            return f"Already transformed!"
        else:
            self.transformed = True
            return f"{self.name} shifts into a sharper form!"
    
    def revert(self):
        if self.transformed is False:
            return f"Already in base form!"
        else:
            self.transformed = False
            return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        TransformCapability.__init__(self)
        Creature.__init__(self, "Morphagon", "Normal/Dragon")

    def attack(self):
        if self.transformed is False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self):
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"
    
    def revert(self):
        self.transformed = False
        return f"{self.name} stabilizes its form."
