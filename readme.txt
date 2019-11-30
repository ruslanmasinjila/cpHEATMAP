
===================
Python Version
===================
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32

===================
INSTALLATION
===================
pip install MetaTrader5
pip install matplotlib
pip install pytz
pip install pandas
pip install seaborn

===================
TODO
===================

- Starting from current UTC time, get N rates for currency pairs from DarwinEx Server using MetaTrader5 API...[DONE]

- For each currency pair, extract the time and the corresponding closing price...[DONE]

- Scale the prices for each currency pair in the table across time between 0 and 1...[DONE]

- Enter the information in pandas table...[DONE]

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
 
- Generate heatmap for the prices...[DONE]



