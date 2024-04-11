class Money:
    def __init__(self, amount: int) -> None:
        self._amount: int = amount

    def __eq__(self, other):
        return (
            self.__class__.__name__ == other.__class__.__name__
            and self._amount == other._amount
        )

    def __ne__(self, other):
        return not self.__eq__(other)
