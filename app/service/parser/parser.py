import argparse

from app.service.parser.parser_output import ParserOutput


class Parser:
    def __init__(self) -> None:
        """Initialize the parser

        Note:
            We define the command line arguments here
        """
        parser = argparse.ArgumentParser(
            description="FizzBuzz CLI",
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
        """Parse the command line arguments

        Returns:
            ParserOutput: The parsed command line arguments

        Note:
            the parse_args() method also shows the help message when the user passes the -h flag
        """
        # Note: the parse_args() method also shows the help message when the user passes the -h flag
        user_input = self.parser.parse_args()
        return ParserOutput(
            namespace=user_input
        )
