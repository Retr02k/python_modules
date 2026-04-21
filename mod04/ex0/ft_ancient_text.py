#!/usr/bin/env python3
import sys


if __name__ == "__main__":
    def main():
        if len(sys.argv) < 2:
            print("Usage: ft_ancient_text.py <file>")
        else:
            try:
                print("=== Cyber Archives Recovery ===")
                print(f"Accessing file: {sys.argv[1]}")
                open_file = open(str(sys.argv[1]), "r")
                content = open_file.read()
                print(content)
                print(f"File {str(sys.argv[1])} closed")
                open_file.close()
            except (FileNotFoundError, PermissionError, Exception) as error_message:
                print(f"Error opening file {sys.argv[1]}: {error_message}")

    main()
