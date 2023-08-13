# Took 87 MB with ridedata, success

import csv
import collections

def read_csv_as_dicts(filename:str, types:list):

    with open(filename, 'r') as f:
        data = csv.reader(f)
        headers = next(data)
        records = DataCollection(headers, types)

        for row in data:
            record = { name: func(val) for name, func, val in zip(headers, types, row) }
            records.append(record)

    return records

# Abstract Base Classes for Containers
class DataCollection(collections.abc.Sequence):
    def __init__(self, headers:list, types:list):
        self.headers = headers
        self.types = types
        # To be { 'head1': [v1, v2, v3], 'head2': [v1, v2, v3], 'head3': [v1, v2, v3] }
        self.data = collections.defaultdict(list)

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.data[self.headers[0]])

    def __getitem__(self, index):
        # Return index value for each header from data dict
        return { head: self.data[head][index] for head in self.headers }

    def append(self, d):
        # Initialize or append to defaultdict columns
        [ self.data[head].append(d[head]) for head in self.headers ]

if __name__ == '__main__':
    import tracemalloc

    tracemalloc.start()
    rows = read_csv_as_dicts('Data/ctabus.csv', [str, str, str, int])
    print(rows[2])
    print(len(rows))
    print(tracemalloc.get_tracemalloc_memory())
