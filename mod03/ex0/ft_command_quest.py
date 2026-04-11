#!/usr/bin/env python3
import sys


print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
arg_count: int = len(sys.argv)
if arg_count > 1:
    print(f"Arguments Received: {arg_count - 1}")
else:
    print("No arguments provided!")
for i in range(1, arg_count):
    print(f"Argument {i}: {sys.argv[i]}")
print(f"Total arguments: {arg_count}")
