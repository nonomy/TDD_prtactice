from src.money import Money


class Dollar(Money):
    def __init__(self, amount: int) -> None:
        super().__init__(amount)

    def times(self, multiplier: int):
        return Dollar(self._amount * multiplier)
