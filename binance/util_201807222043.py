from binance_client import *
import time

client = Client('','')


ret = client.get_asset_balance(asset = 'BNB')
amount = float(ret['free'])
'''
{u'asset': u'BNB', u'free': u'1.87223368', u'locked': u'0.00000000'}
'''


ret = client.get_ticker(symbol='BTCUSDT')
sell1 = float(ret['askPrice'])
buy1 = float(ret['bidPrice'])
'''
{u'askPrice': u'7464.77000000',
 u'askQty': u'0.11896000',
 u'bidPrice': u'7460.94000000',
 u'bidQty': u'0.34830200',
 u'closeTime': 1532260085904,
 u'count': 139813,
 u'firstId': 58053152,
 u'highPrice': u'7487.49000000',
 u'lastId': 58192964,
 u'lastPrice': u'7460.31000000',
 u'lastQty': u'0.00365200',
 u'lowPrice': u'7297.44000000',
 u'openPrice': u'7309.88000000',
 u'openTime': 1532173685904,
 u'prevClosePrice': u'7309.77000000',
 u'priceChange': u'150.43000000',
 u'priceChangePercent': u'2.058',
 u'quoteVolume': u'194634907.11728600',
 u'symbol': u'BTCUSDT',
 u'volume': u'26271.11478200',
 u'weightedAvgPrice': u'7408.70376961'}
'''

ret = client.order_limit_sell(symbol = 'BNBUSDT', quantity = 1.5, price = '16')

ret = client.order_limit_buy(symbol = 'BCCBNB', quantity = '0.025', price = '58')
'''
{u'clientOrderId': u'PFumBG1UaPGrLaX4pRFz45',
 u'cummulativeQuoteQty': u'0.00000000',
 u'executedQty': u'0.00000000',
 u'fills': [],
 u'orderId': 16914067,
 u'origQty': u'0.02500000',
 u'price': u'58.00000000',
 u'side': u'BUY',
 u'status': u'NEW',
 u'symbol': u'BCCBNB',
 u'timeInForce': u'GTC',
 u'transactTime': 1532260361311,
 u'type': u'LIMIT'}
'''

#not chengjiao dingdan
ret = client.get_open_orders(symbol = 'BCCBNB')
orderId = ret[0]['orderId']

'''
[{u'clientOrderId': u'PFumBG1UaPGrLaX4pRFz45',
  u'cummulativeQuoteQty': u'0.00000000',
  u'executedQty': u'0.00000000',
  u'icebergQty': u'0.00000000',
  u'isWorking': True,
  u'orderId': 16914067,
  u'origQty': u'0.02500000',
  u'price': u'58.00000000',
  u'side': u'BUY',
  u'status': u'NEW',
  u'stopPrice': u'0.00000000',
  u'symbol': u'BCCBNB',
  u'time': 1532260361311,
  u'timeInForce': u'GTC',
  u'type': u'LIMIT',
  u'updateTime': 1532260361311}]
'''


ret = client.cancel_order(symbol = 'BCCBNB', orderId = orderId)




