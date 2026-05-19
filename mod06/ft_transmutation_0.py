#!/usr/bin/env python3
import alchemy.transmutation.recipes

print("=== Transmutation 0 ===")
print("Using file alchemy/transmutation/recipes.py directly")
print(f"Testing {alchemy.transmutation.recipes.lead_to_gold.__name__}: "
      f"{alchemy.transmutation.recipes.lead_to_gold()}")
