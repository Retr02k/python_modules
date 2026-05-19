#!/usr/bin/env python3
import alchemy.transmutation

print("=== Transmutation 1 ===")
print("Import transmutation module directly")
print(f"Testing {alchemy.transmutation.recipes.lead_to_gold.__name__}: "
      f"{alchemy.transmutation.recipes.lead_to_gold()}")
