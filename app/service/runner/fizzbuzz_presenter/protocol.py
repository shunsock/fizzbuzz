from typing import Protocol


class FizzBuzzPresenter(Protocol):
    """FizzBuzzPresenter is a protocol that defines the methods
    that a presenter must implement to be treated as a FizzBuzzPresenter.

    Example: Fizz class implements FizzBuzzPresenter
    ```
    class Fizz:
        def __str__(self) -> str:
            return "Fizz"

        def present(self) -> None:
            print(self.__str__())
    ```

    Example: Something class does not implement FizzBuzzPresenter
    ```
    class Something:
        def __str__(self) -> str:
            return "Something"
    ```
    """

    def __str__(self) -> str:
        pass

    def present(self) -> None:
        pass
