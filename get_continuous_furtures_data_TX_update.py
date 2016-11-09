# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 23:06:37 2016

@author: 英哲
"""

import datetime
from shutil import copyfile
import os
import pandas as pd
import quandl

quandl.ApiConfig.api_key = 'txY1sFbHmp6_Bxysscoj' 

month_list = ['F','G','H','J','K','M','N','Q','U','V','X','Z']

#today = datetime.now().date()
today_str = datetime.datetime.now().strftime ("%Y-%m-%d")
today = datetime.datetime.today()

#dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
#TX = pd.read_csv('TX.csv', parse_dates=['datetime'], date_parser=dateparse)
TX = pd.io.parsers.read_csv('TX.csv',index_col='Date', parse_dates=True)
file_last_date = TX.index[-1].strftime ("%Y-%m-%d")
# get current month futures data from quandl
this_month = datetime.datetime.now().month

tail_str = 'TAIFEX/TX' + month_list[this_month] + "2016"
tail = quandl.get(tail_str)
    
# check the last date of current month
last_date = tail.index[-1].date()
# check TX is newest for not
if file_last_date == tail.index[-1].strftime ("%Y-%m-%d"):
    print('data is the newest')
else:
    # crop the data that TX doesn.s include 
    crop = tail.loc[file_last_date:]
    merged = crop[['Open', 'High', 'Low', 'Last', 'Volume', 'Settle']]   # remove "Prev. Day Open 
    # append new data to TX
    #result = TX.append(merged[1:])
    result = [TX, merged[1:] ]
    result = pd.concat(result)
    
    if not os.path.isfile('TX'+file_last_date+'.csv'):
        copyfile('TX.csv','TX'+file_last_date+'.csv')
    result.to_csv('TX.csv') 
    
    twii = quandl.get("YAHOO/INDEX_TWII")
    twii.to_csv('TWII.csv') 

    print('file updated!!!')
    
print('finished')