import requests
import json


re = requests.get('https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=&selectType=&_=1653184876059')

# print(re.json()['data'])
da = re.json()

for i in da['data']:
    print(i[:-1]) # 不輸出季度資料