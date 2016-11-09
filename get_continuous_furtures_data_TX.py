# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:13:03 2016

@author: 英哲
"""

import datetime
import numpy as np
import pandas as pd
import quandl

#wti_near = quandl.get("TAIFEX/TXF2016")
#wti_far = quandl.get("TAIFEX/TXG2016")
'''
df.iloc[-1]
df.loc['2015-12-30':'2015-12-31']
df.iloc[0:-1]
df2.index[-1]
df.loc[df2.index[-1] : df.index[-1] ]
'''

def merge_two_month(head, tail):
    crop = tail.loc[head.index[-1] : tail.index[-1] ]
    final = [head, crop[1:] ]
    result = pd.concat(final)

    return result
    
    
quandl.ApiConfig.api_key = 'txY1sFbHmp6_Bxysscoj' 
    
month_list = ['F','G','H','J','K','M','N','Q','U','V','X','Z']
   
#year = 1999     # which year data 
year = 2015
year_str = str(year)

first_str = 'TAIFEX/TX' + month_list[0] + year_str
first = quandl.get(first_str)

# append other month data to first
for i in range(1, 12):

    #head_str = 'TAIFEX/TX' + month_list[i-1] + year_str
    tail_str = 'TAIFEX/TX' + month_list[i] + year_str
    #head = quandl.get(head_str)
    tail = quandl.get(tail_str)
    first = merge_two_month(first, tail)
    print(tail.tail(1))
    print(first.tail(1))
    
first.to_csv('TX'+year_str+'.csv')

# load back from csv
#load = pd.io.parsers.read_csv('out.csv',index_col='Date')
#merged.equals(load)  # compare two dataframe

# merge all years data
'''
merged = pd.io.parsers.read_csv('TX1999.csv',index_col='Date')
for i in range(2000, 2017):
    year = i
    load2 = pd.io.parsers.read_csv('TX'+str(year)+'.csv',index_col='Date')
    merged = merge_two_month(merged, load2)
    print(i)
    
merged = merged[['Open', 'High', 'Low', 'Last', 'Volume', 'Settle']]   # remove "Prev. Day Open Interest"
merged.to_csv('TX.csv')  
'''