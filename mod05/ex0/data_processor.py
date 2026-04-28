#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any
import ast


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.storage: list[tuple[int, str]] = []
        self.counter: int = -1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise ValueError("Storage is empty")
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            return all(isinstance(element, (int, float)) for element in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Invalid data")
        else:
            if isinstance(data, list):
                for item in data:
                    self.counter += 1
                    self.storage.append((self.counter, str(item)))
            else:
                self.counter += 1
                self.storage.append((self.counter, str(data)))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(isinstance(element, str) for element in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Invalid data")
        else:
            if isinstance(data, list):
                for item in data:
                    self.counter += 1
                    self.storage.append((self.counter, str(item)))
            else:
                self.counter += 1
                self.storage.append((self.counter, str(data)))


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(key, str) for key in data.keys())
        elif isinstance(data, list):
            return all(isinstance(element, dict)
                       and all(isinstance(key, str)
                               for key in element.keys())
                       for element in data)
        return False

    def ingest(self, data: dict[str, Any]) -> None:
        if not self.validate(data):
            raise ValueError("Invalid data")
        else:
            if isinstance(data, list):
                for item in data:
                    self.counter += 1
                    self.storage.append((self.counter, str(item)))
            else:
                self.counter += 1
                self.storage.append((self.counter, str(data)))


if __name__ == "__main__":
    if __name__ == "__main__":
        def main() -> None:
            print("=== Code Nexus - Data Processor ===\n")

            # Test NumericProcessor
            print("Testing Numeric Processor...")
            numeric = NumericProcessor()
            print(f"Trying to validate input '42': {numeric.validate(42)}")
            print(f"Trying to validate input "
                  f"'Hello': {numeric.validate('Hello')}")

            print("Test invalid ingestion of string "
                  "'foo' without prior validation:")
            try:
                numeric.ingest("foo")
            except ValueError as e:
                print(f"Got exception: {e}")

            print("Processing data: [1, 2, 3, 4, 5]")
            numeric.ingest([1, 2, 3, 4, 5])
            print("Extracting 3 values...")
            for i in range(3):
                rank, value = numeric.output()
                print(f"Numeric value {rank}: {value}")

            # Test TextProcessor
            print("\nTesting Text Processor...")
            text = TextProcessor()
            print(f"Trying to validate input '42': {text.validate(42)}")

            print("Processing data: ['Hello', 'Nexus', 'World']")
            text.ingest(['Hello', 'Nexus', 'World'])
            print("Extracting 1 value...")
            rank, value = text.output()
            print(f"Text value {rank}: {value}")

            # Test LogProcessor
            print("\nTesting Log Processor...")
            logs = LogProcessor()
            print(f"Trying to validate input 'Hello': "
                  f"{logs.validate('Hello')}")

            log_data = [
                {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
            ]
            print(f"Processing data: {log_data}")
            logs.ingest(log_data)
            print("Extracting 2 values...")
            for i in range(2):
                rank, value = logs.output()
                log_dict = ast.literal_eval(value)
                formatted = (f"{log_dict['log_level']}: "
                             f"{log_dict['log_message']}")
                print(f"Log entry {rank}: {formatted}")

        main()
