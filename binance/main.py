from binance_client import *
import time

cc = Client('','')
count = 0
flag = 0
while(flag<50000):
    flag = flag +1
    time1 = 1000*time.time()
    aa=cc.get_ticker(symbol='BTCUSDT')
    time2 = 1000*time.time()
    count = count + time2 - time1
    #print(time2-time1, aa)
    print(time2-time1)

print('averge ticker time:', count/50000)
