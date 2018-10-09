#!/usr/bin/python
import numpy as np
import pandas as pd
import tushare as ts
 
print "Begin to get stock data!";
#df = ts.get_hist_data('000875')
df = ts.get_today_all()
#ck = df[['code','name','open','trade','high','low']]
#ck.head(10)
print "Begin to store data!";
ck = df[['code','trade','open','settlement','high','low','volume','amount','per','pb']]
ck.to_csv('stock.csv')