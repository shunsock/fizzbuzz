from app.controller.protocol import ControllerProtocol
from app.service.parser.parser import Parser
from app.service.parser.parser_output import ParserOutput
from app.service.router import Router


def main() -> None:
    """The main function of the CLI app

    Note:
        user_input automatically exit the program with status 2
        when user passes invalid arguments

        controller automatically exit the program with status 1
        when it catches an error
    """
    user_input: ParserOutput = Parser().parse()
    controller: ControllerProtocol = Router.route(user_input)
    controller.run()


if __name__ == "__main__":
    main()
