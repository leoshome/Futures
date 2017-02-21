import pandas as pd
import windows_popup

url = 'http://stock.wearn.com/taifexphoto.asp'
df=pd.read_html(url, encoding = 'big5')
table = df[0]

date = table[0][2:]
fini = table[5][2:]
fini_web = pd.concat([date, fini], axis=1, keys=['date','fini'])
fini_web = fini_web.iloc[::-1]   # reverse table

def date_convert(date):
    #print(date)
    tempdate = date.replace(date[0:3], str(int(date[0:3])+ 1911))
    #print(tempdate)
    return tempdate 

FINI_path = r'C:\Users\Leo\Documents\TAIFEX\FINI\FINI.txt'
FINI_org = pd.read_csv(FINI_path,index_col=False, header=0)

# find final_date of file and locate final_date in web's table
from datetime import datetime
found=0
final_date = FINI_org.iloc[-1][0]
new = FINI_org.copy()
for index, row in fini_web.iterrows():
    tempdate = date_convert(row['date'])   # year+1911
    datetime_web = datetime.strptime(tempdate, '%Y/%m/%d')
    datetime_csv = datetime.strptime(final_date, '%Y/%m/%d')
    #print(tempdate, index)
        
    if datetime_csv == datetime_web and found==0:
        #print(tempdate, index)
        print('found last date corresponding with web data~~')
        found=1
        continue
    if found==1:
        print('new date:',tempdate, row['fini'])
        addt = [ tempdate, 0.0, row['fini'], 0.0, row['fini'], 0.0]
        new.loc[len(new)] = addt   # append new data

if found:        
    new.to_csv(FINI_path, index=False)
    FINI_backup_path = r'C:\Users\Leo\Documents\TAIFEX\FINI\FINI.txt'+ datetime_web.strftime('%Y%m%d')
    new.to_csv(FINI_backup_path, index=False)     

print('done')
if found==0:
    print('WARNING!!!!!!!!!!!!!!!!!!!!!!!  Please check web data or TXT')
    balloon_tip('!!!FINI WARNING!!!', 'Please check web data or TXT')
    