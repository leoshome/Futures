# -*- coding: utf-8 -*-
"""
example from : http://yvictor.logdown.com/posts/996770
用python爬期交所期貨選擇權即時資料
"""

from selenium import webdriver

#driver = webdriver.PhantomJS(executable_path=r'C:\Users\Leo\AppData\Roaming\npm\node_modules\phantomjs\lib\phantom\bin\phantomjs.exe')
phantomjs_path = r'C:\Users\Leo\AppData\Roaming\npm\node_modules\phantomjs\lib\phantom\bin\phantomjs.exe'
driver  = webdriver.PhantomJS(phantomjs_path)

driver.get('http://info512.taifex.com.tw/Future/OptQuote_Norl.aspx')

from bs4 import BeautifulSoup
import pandas as pd
soup = BeautifulSoup(driver.page_source,'lxml')
pd.read_html(str(soup.select('#divDG')[0]),header=0)[0].loc[10:20]

selectbox = webdriver.support.ui.Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$ddlFusa_SelMon'))
selectbox.all_selected_options
[sel.text for sel in selectbox.options]

selectbox.select_by_value([sel.text for sel in selectbox.options][1])

# 看看PAGE_SOURCE中的報價是否變成次月
soup = BeautifulSoup(driver.page_source,'lxml')
pd.read_html(str(soup.select('#divDG')[0]),header=0)[0].loc[10:20]

