class Buzz:
    def __str__(self) -> str:
        return "Buzz"

    def present(self) -> None:
        print(self.__str__())