from app.controller.fizzbuzz import FizzbuzzController
from app.controller.protocol import ControllerProtocol
from app.service.parser.parser_output import ParserOutput


class Router:
    def __init__(self) -> None:
        pass

    @staticmethod
    def route(user_input: ParserOutput) -> ControllerProtocol:
        return FizzbuzzController(
            start = user_input.namespace.start,
            end = user_input.namespace.end
        )