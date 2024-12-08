from app.controller.fizzbuzz import FizzbuzzController
from app.controller.protocol import ControllerProtocol


class Router:
    def __init__(self) -> None:
        pass

    @staticmethod
    def route(user_input) -> ControllerProtocol:
        return FizzbuzzController(
            start = user_input.namespace.start,
            end = user_input.namespace.end
        )