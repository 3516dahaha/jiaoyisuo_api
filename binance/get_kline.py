from binance_client import *
import time
import hmac
import hashlib
import time
import json, requests


#1503014400000  20170818 ms
binance_start = 1503014400000
st = time.localtime(binance_start/1000)
binance_start_date = time.strftime('%Y%m%d', st)
ts_now = time.time()*1000
day_date_ts = []
ts_day = binance_start
while(ts_day < ts_now):
    #print(ts_day)
    date_day = time.strftime('%Y%m%d', time.localtime(ts_day/1000))
    ll = []
    ll.append(date_day)
    ll.append(ts_day)
    day_date_ts.append(ll)
    ts_day = ts_day + 1000*60*60*24

print(day_date_ts[:10])
    


para = []
with open('private/conf.txt', 'r') as f:
    for line in f.readlines():
        para.append(line.strip())
client = Client(para[0],para[1])

for i, val in enumerate(day_date_ts):
    if(i==len(day_date_ts)-1):
        break
    klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1MINUTE, val[1], val[1]+1000*60*60*24)
    file_out = 'private/klines/{0}'.format(val[0])
    with open(file_out, 'w') as f:
        for kl in klines:
            ts_close = kl[6]
            price_close = kl[4]
            f.write(str(ts_close))
            f.write('\t')
            f.write(price_close)
            f.write('\n')
            


