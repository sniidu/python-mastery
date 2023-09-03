from abc import ABC, abstractmethod


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(" ".join("%10s" % h for h in headers))
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        print(" ".join("%10s" % d for d in rowdata))


class CsvTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(h for h in headers))

    def row(self, rowdata):
        print(",".join(str(d) for d in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr> <th>", "</th> <th>".join(h for h in headers), "</th> </tr>", sep="")

    def row(self, rowdata):
        print(
            "<tr> <td>",
            "</td> <td>".join(str(d) for d in rowdata),
            "</td> </tr>",
            sep="",
        )


class ColumnFormatMixin:
    formats = []

    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


class UpperHeadersMixin:
    # Heading is first passed to this which
    # super's it to next class in uppercase
    # class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter)
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


def create_formatter(type: str, column_formats=None, upper_headers=None):
    map = {
        "html": HTMLTableFormatter,
        "csv": CsvTableFormatter,
        "text": TextTableFormatter,
    }
    formatter = map[type]
    if column_formats:

        class formatter(ColumnFormatMixin, formatter):
            formats = column_formats

    if upper_headers:

        class formatter(UpperHeadersMixin, formatter):
            pass

    return formatter()


def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


if __name__ == "__main__":
    import stock, reader, tableformat

    portfolio = reader.read_csv_as_instances("Data/portfolio.csv", stock.Stock)
    formatter = tableformat.create_formatter("csv")
    tableformat.print_table(portfolio, ["name", "shares", "price"], formatter)
