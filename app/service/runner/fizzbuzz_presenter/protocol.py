from typing import Protocol


class FizzBuzzPresenter(Protocol):
    def __str__(self) -> str:
        pass

    def present(self) -> None:
        pass