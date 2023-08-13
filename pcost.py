import sys

def portfolio_cost(filename):
    whole = 0
    with open(filename, 'r') as f:
        for line in f:
            listed = line.split()
            try:
                stocks = int(listed[1])
                price = float(listed[2])
            except ValueError as e:
                print("Couldn't parse: ", listed)
                print("Reason: ", e)
            whole += stocks * price
        return whole

if __name__ == '__main__':
    print(portfolio_cost(sys.argv[1]))
