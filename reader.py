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

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
