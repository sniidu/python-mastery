class Structure:
    _fields = ()

    def __init__(self, *args) -> None:
        if len(self._fields) != len(args):
            e = f"Expected {len(self._fields)} arguments"
            raise TypeError(e)
        for field, arg in zip(self._fields, args):
            self.__setattr__(field, arg)


class Stock(Structure):
    _fields = ("name", "shares", "price")


if __name__ == "__main__":
    s = Stock("GOOG", 199, 34.23)
    s2 = Stock("GOOG", 34.23)
