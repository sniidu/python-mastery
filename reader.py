import csv
from typing import List


def read_csv_as_dicts(filename, types: List[str], header=None):
    """
    Read CSV data into a list of dictionaries with optional type conversion
    """
    with open(filename) as file:
        return csv_as_dicts(file, types, header)


def read_csv_as_instances(filename, cls):
    """
    Read CSV data into a list of instances
    """
    with open(filename) as file:
        return csv_as_instances(file, cls)


def csv_as_dicts(lines, types, header=None):
    rows = csv.reader(lines)
    if not header:
        headers = next(rows)
    else:
        headers = header
    records = []
    for row in rows:
        record = {name: func(val) for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records


def csv_as_instances(lines, cls):
    rows = csv.reader(lines)
    _ = next(rows)
    records = []
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records


if __name__ == "__main__":
    file = open("Data/portfolio.csv")
    port = csv_as_dicts(file, [str, int, float])
    print(port)
