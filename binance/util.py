from binance_client import *
import time

client = Client('','')


ret = client.get_asset_balance(asset = 'BNB')
amount = float(ret['free'])


ret = client.get_ticker(symbol='BTCUSDT')
sell1 = float(ret['askPrice'])
buy1 = float(ret['bidPrice'])

ret = client.order_limit_sell(symbol = 'BNBUSDT', quantity = 1.5, price = '16')

ret = client.order_limit_buy(symbol = 'BCCBNB', quantity = '0.025', price = '58')


ret = client.get_open_orders(symbol = 'BCCBNB')
orderId = ret[0]['orderId']

