import csv
import logging
from typing import List, TextIO

logging.basicConfig(level=logging.DEBUG)


def read_csv_as_dicts(filename: str, types: List[str], header=None):
    """
    Read CSV data into a list of dictionaries with optional type conversion
    """
    with open(filename) as file:
        return csv_as_dicts(file, types, header)


def read_csv_as_instances(filename: str, cls):
    """
    Read CSV data into a list of instances
    """
    with open(filename) as file:
        return csv_as_instances(file, cls)


def csv_as_dicts(lines: TextIO, types: List, header=None):
    return convert_csv(
        lines,
        lambda headers, row: {
            name: func(val) for name, func, val in zip(headers, types, row)
        },
    )


def csv_as_instances(lines: TextIO, cls, headers=None):
    return convert_csv(lines, lambda headers, row: cls.from_row(row))


def convert_csv(lines, con, headers=None):
    rows = csv.reader(lines)
    records = []
    if not headers:
        headers = next(rows)
    for i, row in enumerate(rows):
        try:
            records.append(con(headers, row))
        except ValueError as e:
            logging.warning(f"Row {i + 1}: Bad row: {row}")
            logging.debug(f"Row {i + 1}: Reason: {e}")
            continue
    return records


def make_dict(headers, row):
    return dict(zip(headers, row))


if __name__ == "__main__":
    file = open("Data/portfolio.csv")
    port = csv_as_dicts(file, [str, int, float])
    print(port)

    problem = read_csv_as_dicts("Data/missing.csv", types=[str, int, float])
