class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()
    
def print_table(seq:list, attr:list):
    print(' '.join('%10s' % field for field in attr))
    print(('-' * 10 + ' ') * len(attr))
    for s in seq:
        print(' '.join('%10s' % getattr(s, field) for field in attr))

if __name__ == '__main__':
    import stock
    portfolio = stock.read_portfolio('Data/portfolio.csv')
    print_table(portfolio, ['name','price'])
