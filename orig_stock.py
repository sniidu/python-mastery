import csv


class Stock:
    _types = [str, int, float]
    __slots__ = ["name", "_shares", "_price"]

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        # Neat oneliner for this ought to be working
        return f"{self.__class__.__name__}({','.join(str(getattr(self, s)) for s in self.__init__.__code__.co_names)})"

    def __eq__(self, other):
        return isinstance(other, Stock) and (
            (self.name, self.shares, self.price)
            == (other.name, other.shares, other.price)
        )

    @classmethod
    def from_row(cls, row):
        """Alternative initiator"""
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            err_msg = f"Expected {self._types[1]}"
            raise TypeError(err_msg)
        elif value < 0:
            raise ValueError("Shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            err_msg = f"Expected {self._types[2]}"
            raise TypeError(err_msg)
        elif value < 0:
            raise ValueError("Price must be >= 0")
        self._price = value

    def sell(self, num_of_shares: int):
        self.shares -= num_of_shares


def print_portfolio(portfolio: list):
    print("%10s %10s %10s" % ("name", "shares", "price"))
    print("%10s %10s %10s" % ("----------", "----------", "----------"))
    for s in portfolio:
        print("%10s %10d %10.2f" % (s.name, s.shares, s.price))


def read_portfolio(filename, cls=Stock):
    portfolios = []
    with open(filename) as f:
        data = csv.reader(f)
        _ = next(data)
        for name, shares, price in data:
            portfolios.append(cls.from_row([name, shares, price]))
    return portfolios


if __name__ == "__main__":
    p = read_portfolio("Data/portfolio.csv")
