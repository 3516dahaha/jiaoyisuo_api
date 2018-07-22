from okex_client import *


# set the parameters to limit the number of bids or asks
parameters = {'limit_asks': 5, 'limit_bids': 5}

# create the client
client = OkexClient(None, None)

# symbol to query the order book
symbol = 'ltc_btc'
# get latest ticker
ticker = client.ticker(symbol)

flag = 0
count = 0
while(flag<50000):
    flag= flag+1
    time1 = time.time()*1000
    ticker = client.ticker('btc_usdt')
    time2 = time.time()*1000
    print(time2-time1)
    count = count + time2-time1
    #print(time2-time1, ticker)

print('averge ticker time:', count/50000)
