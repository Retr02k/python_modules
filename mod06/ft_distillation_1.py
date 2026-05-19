import alchemy

print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potions")
print(f"Testing {alchemy.strength_potion.__name__}: "
      f"{alchemy.strength_potion()}")
print(f"Testing heal alias: {alchemy.heal()}")
