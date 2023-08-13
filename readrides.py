import csv
import collections
import tracemalloc

def read_rides_as_dict(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
                }
            records.append(record)
    return records

# Abstract Base Classes for Containers
class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        if isinstance(index, slice):
            step = 1 if index.step is None else index.step
            # No idea how to return RideData object like in example
            return [
                    dict(
                        route = self.routes[i],
                        date = self.dates[i],
                        daytype = self.daytypes[i],
                        rides = self.numrides[i]
                    ) for i in range(index.start, index.stop, step)
                ]
        return { 'route': self.routes[index],
                 'date': self.dates[index],
                 'daytype': self.daytypes[index],
                 'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

if __name__ == '__main__':
    tracemalloc.start()
    rows = read_rides_as_dict('Data/ctabus.csv')
    print(tracemalloc.get_traced_memory())
