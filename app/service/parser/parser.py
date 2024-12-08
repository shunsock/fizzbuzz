import argparse
import io

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
            help_message=self.get_print_help_as_string()
        )

    def get_print_help_as_string(self) -> str:
        # Create an in-memory file object
        buffer = io.StringIO()

        # Redirect print_help() output to the buffer
        self.parser.print_help(file=buffer)

        # Retrieve the content of the buffer as a string
        return buffer.getvalue()
