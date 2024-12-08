from argparse import Namespace
from typing import Final

from app.controller.protocol import ControllerProtocol
from app.service.parser.parser import Parser
from app.service.parser.parser_output import ParserOutput
from app.service.router import Router


def main() -> None:
    user_input: Final[ParserOutput] = Parser().parse()
    controller: ControllerProtocol = Router.route(user_input)
    controller.run()


if __name__ == "__main__":
    main()
