from datetime import datetime
from MetaTrader5 import *
from pytz import timezone
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



#==================================================
#INITIALIZATION OF MT5 TERMINAL
#==================================================

# connect to MetaTrader 5
# Log into MetaTrader if necessary
MT5Initialize()


# wait till MetaTrader 5 connects to the trade server
MT5WaitForTerminal()


# display data on connection status, server name and trading account
print(MT5TerminalInfo())


# display data on MetaTrader 5 version
print(MT5Version())


#==================================================
# GETTING RATES FROM MT5 TERMINAL
#==================================================

# Read currency pair names from the file into a list
currency_pairs = [currency_pair.rstrip('\n') for currency_pair in open("currency_pairs.txt")]


# get current UTC time
utc_from = datetime.utcnow()

rates = []
N = 100

for i in currency_pairs:
	print("Getting rates for:",i)
	rates.append(MT5CopyRatesFrom(i, MT5_TIMEFRAME_H1, utc_from, N))
	  
	
#==================================================
# SHUTTING DOWN MT5 TERMINAL
#==================================================

# shut down connection to the MetaTrader 5 terminal
MT5Shutdown()


#==================================================
# PROCESSING DATA FROM MT5 TERMINAL
#==================================================

# Initialization of pandas dataframe for currency pairs and their closing prices
cpTABLE = pd.DataFrame(index = currency_pairs, columns = [i[0] for i in rates[0]])


# POPULATE THE TABLE
for i in range(len(rates)):			# For every currency pair

	closing_prices = []
	for j in rates[i]:		    	# For every rate in the current currency pair
		closing_prices.append(j[4])	# Closing price is at index 4 of every rate
	
	# Scale closing prices between 0 and 1
	scaled_closing_prices = [(x-min(closing_prices))/(max(closing_prices)-min(closing_prices)) for x in closing_prices]
	
	# Insert the scaled closing prices into table at the corresponding  currency pair
	cpTABLE.loc[currency_pairs[i],:] = scaled_closing_prices
	



# Convert DataFrame value types from object to float
cpTABLE = cpTABLE[cpTABLE.columns].astype(float)

# Display the table
print(cpTABLE.index)

# Create heatmap of the table
sns.heatmap(cpTABLE, xticklabels=True, yticklabels=True, cmap="RdYlGn")

# Display the heatmap
plt.show()


