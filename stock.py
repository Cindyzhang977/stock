from yahoo_fin.stock_info import *

class Player:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.stocks = {}

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_balance(self):
        return self.balance

    def view_stocks(self):
        for item in self.stocks:
            print('{:10s} {:1s}'.format(item, '%.2f'%(self.stocks[item])))

    def add_balance(self, amount):
        self.balance += amount
        return 'Balance is now {0}'.format(self.balance)

    def purchase(self, ticker, shares):
        assert type(shares) == int ,'must buy whole number of shares'
        price = get_live_price(ticker)
        if (self.balance - price * shares) >= 0:
            self.stocks[ticker] = self.stocks.get(ticker, 0) + shares
            self.balance -= price * shares
        else:
            return 'not enough money'

        return "new balance: " + str(self.balance)

    def sell(self, ticker, shares):
        assert type(shares) == int ,'must sell whole number of shares'
        price = get_live_price(ticker)
        if ticker in self.stocks.keys():
            if shares <= self.stocks[ticker]:
                self.stocks[ticker] = self.stocks[ticker] - shares
                if self.stocks[ticker] == 0:
                    self.stocks.pop(ticker)
                self.balance += price * shares
            else:
                return 'not enough shares'
        else:
            return stock.name + ' not found'

        return "Sold {0} shares of {1}. Earned {2}".format(shares, ticker, price*shares)
