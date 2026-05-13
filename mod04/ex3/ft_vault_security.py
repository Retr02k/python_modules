#!/usr/bin/env python3
from typing import Tuple

if __name__ == "__main__":
    def secure_archive(file_name: str,
                       operation: str,
                       content: str = ""
                       ) -> Tuple[bool, str]:
        if operation == "read":
            try:
                with open(file_name, "r") as file:
                    return True, file.read()
            except (FileNotFoundError, PermissionError) as error_message:
                return False, f"{error_message}"
        elif operation == "write":
            try:
                with open(file_name, "w") as file:
                    file.write(content)
                    return True, f"content written to {file_name}"
            except (FileNotFoundError, PermissionError) as error_message:
                return False, f"{error_message}"
        return False, "Invalid operation"

    def main() -> None:
        print("Using 'secure_archive' to read from a nonexistent file:")
        print(secure_archive("i_do_not_exist", "read"))
        print()
        print("Using 'secure_archive' to read from an inaccessible file:")
        print(secure_archive("/etc/master.passwd", "read"))
        print()
        print("Using 'secure_archive' to read from a regular file:")
        print(secure_archive("ancient_fragment.txt", "read"))
        print()
        print("Using 'secure_archive' to write previous "
              "content to a new file:")
        print(secure_archive("gabriel", "write", "ancient_fragment.txt"))

main()
