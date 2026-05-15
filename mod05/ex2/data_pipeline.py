#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Protocol, Any
import ast


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        results = []
        for integer, string in data:
            if string.startswith('{'):
                dict_obj = ast.literal_eval(string)
                formatted = ': '.join(str(v) for v in dict_obj.values())
                results.append(formatted)
            else:
                results.append(string)
        csv_line = ','.join(results)
        print(f"CSV Output: \n{csv_line}")


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json_dict = {}
        for integer, string in data:
            if string.startswith('{'):
                dict_obj = ast.literal_eval(string)
                formatted = ': '.join(str(v) for v in dict_obj.values())
                json_dict[f"item_{integer}"] = formatted
            else:
                json_dict[f"item_{integer}"] = string
        print(f"JSON Output: \n{json_dict}")


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


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False
            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    processed = True
                    break
            if not processed:
                print(f"DataStream error - "
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
        for processor in self.processors:
            total_processed = (processor.counter + 1)
            remaining = len(processor.storage)
            print(f"{processor.__class__.__name__}: total {total_processed} "
                  f"items processed, remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        consumable = 0
        tuple_list = []
        for processor in self.processors:
            while consumable < nb:
                try:
                    tuple_list.append(processor.output())
                except Exception:
                    break
                consumable += 1
            plugin.process_output(tuple_list)
            tuple_list.clear()
            consumable = 0


if __name__ == "__main__":
    def main() -> None:
        first_batch = ['Hello world',
                       [3.14, -1, 2.71],
                       [{'log_level': 'WARNING',
                         'log_message': 'Telnet access! Use ssh instead'},
                        {'log_level': 'INFO',
                         'log_message': 'User wil is connected'}],
                       42,
                       ['Hi', 'five']]
        print("=== Code Nexus - Data Pipeline ===\n")
        print("Initialize Data Stream...\n")
        print("== DataStream statistics ==")
        stream = DataStream()
        stream.print_processors_stats()

        print("\nRegistering Processors")
        numeric = NumericProcessor()
        text = TextProcessor()
        log = LogProcessor()
        stream.register_processor(numeric)
        stream.register_processor(text)
        stream.register_processor(log)

        print(f"\nSend first batch of data on stream: {first_batch}\n")
        stream.process_stream(first_batch)
        print("== DataStream statistics ==")
        stream.print_processors_stats()

        nb = 3
        print(f"\nSend {nb} processed data "
              f"from each processor to a CSV plugin:")
        csv_plugin = CSVExportPlugin()
        stream.output_pipeline(nb, csv_plugin)
        print("\n== DataStream statistics ==")
        stream.print_processors_stats()

        another_batch = [21,
                         ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                         [{'log_level': 'ERROR',
                           'log_message': '500 server crash'},
                          {'log_level': 'NOTICE',
                           'log_message': 'Certificate expires in 10 days'}],
                         [32, 42, 64, 84, 128, 168], 'World hello']
        print(f"\nSend another batch of data {another_batch}\n")

        print("== DataStream statistics ==")
        stream.process_stream(another_batch)
        stream.print_processors_stats()
        nb = 5
        print(f"\nSend {nb} processed data "
              f"from each processor to a JSON plugin:")
        json_plugin = JSONExportPlugin()
        stream.output_pipeline(nb, json_plugin)

        print("\n== DataStream statistics ==")
        stream.print_processors_stats()

    main()
