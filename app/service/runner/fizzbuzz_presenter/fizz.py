class Fizz:
    def __str__(self) -> str:
        return "Fizz"

    def present(self) -> None:
        print(self.__str__())
