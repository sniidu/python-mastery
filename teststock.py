import unittest
import stock


class TestStock(unittest.TestCase):
    def test_create(self):
        # Static
        s = stock.Stock("GOOG", 100, 490.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
        self.assertEqual(s.cost, 49010)
        self.assertEqual(s.__repr__(), "Stock(GOOG,100,490.1)")

        # Sell method
        s.sell(20)
        self.assertEqual(s.shares, 80)

        # From_row method
        s2 = stock.Stock.from_row(["AAPL", 20, 230.2])
        self.assertEqual(s2.name, "AAPL")

        # eq method
        self.assertEqual(s == s2, False)

    def test_bad_shares(self):
        s = stock.Stock("GOOG", 100, 490.1)
        with self.assertRaises(TypeError):
            s.price = "arts"

        with self.assertRaises(ValueError):
            s.price = -30.234

        with self.assertRaises(TypeError):
            s.shares = 234.234

        with self.assertRaises(ValueError):
            s.shares = -30

        with self.assertRaises(AttributeError):
            s.arst = -30


if __name__ == "__main__":
    unittest.main()
