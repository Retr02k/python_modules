from alchemy.potions import healing_potion, strength_potion

print("=== Distillation 0 ===")
print("Direct access to alchemy/potions.py")
print(f"Testing {strength_potion.__name__}: {strength_potion()}")
print(f"Testing {healing_potion.__name__}: {healing_potion()}")
