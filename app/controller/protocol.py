from typing import Protocol


class ControllerProtocol(Protocol):
    def run(self) -> None:
        pass