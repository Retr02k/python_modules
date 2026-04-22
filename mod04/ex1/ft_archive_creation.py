#!/usr/bin/env python3
import sys


if __name__ == "__main__":
    def main() -> None:
        if len(sys.argv) < 2:
            print("Usage: ft_ancient_text.py <file>")
        else:
            print("=== Cyber Archives Recovery & Preservation ===")
            print(f"Accessing file '{sys.argv[1]}'\n---\n")
            try:
                open_file = open(sys.argv[1], "r")
                file_read = open_file.read()
                print(file_read)
                open_file.close()
                print(f"---\nFile '{sys.argv[1]}' closed.\n")
            except (FileNotFoundError,
                    PermissionError,
                    Exception) as error_message:
                print(f"Error opening file {sys.argv[1]}: {error_message}")
            try:
                print("Transform data:\n---\n")
                temp_file = []
                with open(sys.argv[1], "r") as file:
                    while True:
                        line = file.readline()
                        if not line:
                            break
                        print(f"{line[:-1]}#")
                        temp_file.append(line[:-1] + "#\n")
                file_to_write_to = input("\n---\nEnter new file "
                                         "name (or empty): ")
                if not file_to_write_to:
                    print("Not saving data")
                    return
                new_file = open(file_to_write_to, "w")
                for i in temp_file:
                    new_file.write(i)
                print(f"Saving data to '{file_to_write_to}'")
                print(f"Data saved in file '{file_to_write_to}'.")
                new_file.close()
            except (FileNotFoundError,
                    PermissionError,
                    Exception) as error_message:
                print(f"Error opening file {sys.argv[1]}: {error_message}")

    main()
