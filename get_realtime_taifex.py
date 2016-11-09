# -*- coding: utf-8 -*-
"""

台灣期貨指數即時報價
"""

# -*- coding: utf-8 -*-
#from __future__ import absolute_import, division, print_function, unicode_literals

#from urllib.request import urlopen
from time import sleep
#from sys import exit
from datetime import datetime, time
#from bs4 import BeautifulSoup
import telegram
import pandas as pd

# telegram bot define
account = 'mobile'
chat_id = 241715446
token = "266762115:AAEg7BStlN0R98bO1ptQFcWY2TPeK6tvBOE"

def sendout(msg):
    # Telegram Bot Authorization Token
    bot = telegram.Bot(token)
    global chat_id
    bot.sendMessage(chat_id=chat_id, text=msg)
# end of send message function define

TXF_NAME = u'臺指現貨'
target_times = 0

url = 'http://info512.taifex.com.tw/Future/FusaQuote_Norl.aspx'

while target_times < 3:
    
    now = datetime.now()
    now_time = now.time()
    '''
    if time(8,45) <= now_time <= time(13,45):        
        print("yes, within the interval")
    else:
        print("Non-business time")
        break
       ''' 
    df=pd.read_html(url, encoding = 'utf-8')
    
    twii_name = df[0].ix[18][0]  # 臺指現貨  
    twii_current = df[0].ix[18][6]   # 臺指現貨  成交價
    future_name = df[0].ix[19][0]  # 臺指期116
    future_near = df[0].ix[19][6]   # 臺指期116  成交價
    
    print(twii_name + ":" + twii_current)
    print(future_name + ": " + future_near)
    
    if twii_name == TXF_NAME and twii_current < future_near:
        target_times = target_times + 1
        print("Hit times:" , target_times)
        if target_times > 0:
            print("Signal is acheive, Now time is " + now.ctime())
            #print("價差:", int(float(twii_current) - float(future_near)))
            msg  = "價差:" + str(int(float(twii_current) - float(future_near)))
            print(msg)
            sendout(msg)

    sleep(60)

print("press any key to exit")
input()
#sendout('testing ')