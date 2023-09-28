from structure import Structure


class Stock(Structure):
    _fields = ("name", "shares", "price")

    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= shares


if __name__ == "__main__":
    s = Stock(name="AAPL", price=1239.1, shares=23)
