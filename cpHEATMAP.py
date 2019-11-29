from datetime import datetime
from MetaTrader5 import *
from pytz import timezone
import matplotlib.pyplot as plt

 
# connect to MetaTrader 5
# Log into MetaTrader if necessary
MT5Initialize()


# wait till MetaTrader 5 connects to the trade server
MT5WaitForTerminal()


# display data on connection status, server name and trading account
print(MT5TerminalInfo())


# display data on MetaTrader 5 version
print(MT5Version())

# Read currency pair names from the file into a list
currency_pairs = [currency_pair.rstrip('\n') for currency_pair in open("currency_pairs.txt")]


# get current UTC time
utc_from = datetime.utcnow()

rates = []
N = 1000

for i in currency_pairs:
	print("Getting rates for:",i)
	rates.append(MT5CopyRatesFrom(i, MT5_TIMEFRAME_H1, utc_from, N))
	  

# shut down connection to the MetaTrader 5 terminal
MT5Shutdown()

