import argparse

from app.service.parser.parser_output import ParserOutput


class Parser:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(
            description="This is a simple CLI app"
        )

        parser.add_argument(
            "--start",
            type=int,
            default=1,
            help="The start of the FizzBuzz sequence"
        )

        parser.add_argument(
            "--end",
            type=int,
            default=100,
            help="The upper bound for the FizzBuzz sequence",
        )

        self.parser = parser

    def parse(self) -> ParserOutput:
        return ParserOutput(
            namespace=self.parser.parse_args(),
        )
