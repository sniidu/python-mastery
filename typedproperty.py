def typedproperty(expected_type, name=None):
    # def __set_name__(self, name):
    #     self.name = name
    #     nonlocal private_name
    #     private_name = "_" + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f"Expected {expected_type}")
        setattr(self, private_name, val)

    return value


def String():
    return typedproperty(str)


def Float():
    return typedproperty(float)


def Integer():
    return typedproperty(int)


if __name__ == "__main__":

    class Stock:
        name = String()
        shares = Integer()
        price = Float()

        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

    s = Stock("asdf", 12.2, "asdf")
