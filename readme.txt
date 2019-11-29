INSTALLATION
- pip install MetaTrader5
- pip install matplotlib
- pip install pytz
- pip install pandas


TODO:
- Starting from current UTC time, get N rates for currency pairs from DarwinEx Server using MetaTrader5 API...[DONE]


- For each currency pair, extract the time and the corresponding closing price. Enter the information in pandas table...[DONE]

 -------------- ----------------------------------------
|currency_pair | time1 | time2 | time3 | time4 | timeN  |
 -------------- ----------------------------------------
| pair1        |       |       |       |       |        |
---------------------------------------------------------
| pair2        |       |       |       |       |        |
---------------------------------------------------------
| pair3        |       |       |       |       |        |
---------------------------------------------------------
| pair4        |       |       |       |       |        |
---------------------------------------------------------
| pairN        |       |       |       |       |        |
---------------------------------------------------------


- Scale the prices for each currency pair in the table across time between 0 and 1

 
- Generate heatmap for the prices



