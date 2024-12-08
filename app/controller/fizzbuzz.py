class FizzbuzzController:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def run(self) -> bool:
        print("FizzbuzzController is running")
        print(f"Start: {self.start}")
        print(f"End: {self.end}")
        return True