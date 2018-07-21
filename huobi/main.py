from huobi_client import *
import time

flag = 0
count = 0

while(flag<10):
    flag = flag +1
    time1 = time.time()*1000
    aa = get_ticker('btcusdt')
    time2 = time.time()*1000
    count = count + time2 - time1
    print(time2-time1)
    #print(time2-time1, aa)

print('averge ticker time:', count/10000)


