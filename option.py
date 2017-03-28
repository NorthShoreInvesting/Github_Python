import pandas as pd
from pandas_datareader.data import Options
import datetime as dt
'''
PRECONDITIONAL ASSUMPTIONS:
1. There are no associated transaction costs to factor in
2. All trading profits (net of trading losses), are subject to the same tax rate
3. Borrowing & Lending is possible at the risk intrest rate
'''


class leg:
	def __init__(self, ticker, ask, bid, strike, expiration):

		self.ticker = ticker
		self.ask = ask
		self.bid = bid
		self.strike = strike
		self.expiration = expiration


'''
Pandas_Datareader returns a dataframe with formatted
option data. Uses a heriarchial index to allow for easy
and specific access of information
'''
ticker = Options('amzn','yahoo')
expiration_dates = ticker.expiry_dates
data = ticker.get_all_data()

yr =2017
mon = 4
day =21
exp_date = dt.datetime(yr, mon, day)
kind = 'call'


raw = data.loc[(900,exp_date,kind),['Ask','Bid']]
bid = float(raw.xs('Bid', axis = 1))
ask = float(raw.xs('Ask', axis = 1))
print(str(ask) +' | '+str(bid))