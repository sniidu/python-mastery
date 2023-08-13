import csv

def read_csv_as_dicts(filename:str, types:list):

    records = []
    with open(filename, 'r') as f:
        data = csv.reader(f)
        headers = next(data)

        for row in data:
            record = { name: func(val) for name, func, val in zip(headers, types, row) }
            records.append(record)

    return records
