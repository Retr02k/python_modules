#!/usr/bin/env python3

from ex0.data_processor import (DataProcessor,
                                NumericProcessor,
                                TextProcessor,
                                LogProcessor)
import typing


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
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


if __name__ == "__main__":
    def main():
        first_batch = ['Hello world',
                       [3.14, -1, 2.71],
                       [{'log_level': 'WARNING',
                         'log_message': 'Telnet access! Use ssh instead'},
                        {'log_level': 'INFO',
                         'log_message': 'User wil is connected'}],
                       42,
                       ['Hi', 'five']]
        print("=== Code Nexus - Data Stream ===\n")
        print("Initialize Data Stream...")
        print("== DataStream statistics ==")
        stream = DataStream()
        stream.print_processors_stats()

        print("\nRegistering Numeric Processor")
        numeric = NumericProcessor()
        stream.register_processor(numeric)
        print(f"\nSend first batch of data on stream: {first_batch}")
        stream.process_stream(first_batch)
        print("== DataStream statistics ==")
        stream.print_processors_stats()

        print("\nRegistering other data processors")
        text = TextProcessor()
        log = LogProcessor()
        stream.register_processor(text)
        stream.register_processor(log)
        print("Send the same batch again")
        stream.process_stream(first_batch)
        print("== DataStream statistics ==")
        stream.print_processors_stats()

        numeric_counter = 0
        for i in range(3):
            numeric.output()
            numeric_counter += 1
        text_counter = 0
        for i in range(2):
            text.output()
            text_counter += 1
        log_counter = 0
        for i in range(1):
            log.output()
            log_counter += 1
        print(f"\nConsume some elements from the data processors: "
              f"Numeric {numeric_counter}, "
              f"Text {text_counter}, "
              f"Log {log_counter}")
        print("===Data Stream statistics ==")
        stream.print_processors_stats()

    main()
