from binance_client import *
import time
import hmac
import hashlib
import time
import json, requests


para = []
with open('private/conf.txt', 'r') as f:
    for line in f.readlines():
        para.append(line.strip())
client = Client(para[0],para[1])


ret = client.get_asset_balance(asset = 'BNB')
amount = float(ret['free'])


url='https://api.binance.com/api/v1/ticker/24hr'
payload = {'symbol': 'BTCUSDT'}
ret = requests.get(url, params=payload)
ret = client.get_ticker(symbol='BTCUSDT')
sell1 = float(ret.json()['askPrice'])
buy1 = float(ret.json()['bidPrice'])

ret = client.order_limit_sell(symbol = 'BNBUSDT', quantity = 1.5, price = '19')#post  jiaoyi api

ret = client.order_limit_buy(symbol = 'BCCBNB', quantity = '0.025', price = '58')#post  jiaoyi api


ret = client.get_open_orders(symbol = 'BNBUSDT')#get chaxun only api
orderId = ret[0]['orderId']


ret = client.cancel_order(symbol = 'BNBUSDT', orderId = orderId)#jiaoyi api


API_SECRET=para[1]
def _order_params(data):
    has_signature = False
    params = []
    for key, value in data.items():
        if key == 'signature':
            has_signature = True
        else:
            params.append((key, value))
    # sort parameters by key
    params.sort(key=itemgetter(0))
    if has_signature:
        params.append(('signature', data['signature']))
    return params


def _generate_signature(data):
    ordered_data = _order_params(data)
    query_string = '&'.join(["{}={}".format(d[0], d[1]) for d in ordered_data])
    m = hmac.new(API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256)
    return m.hexdigest()

session.headers.update({'Accept': 'application/json',
                                'User-Agent': 'binance/python',
                                'X-MBX-APIKEY': self.API_KEY})

kwargs['data']['signature'] = _generate_signature(kwargs['data'])

'signature', '37aa2bb7cd3d2efcdf444d05c1d1abdb5cdc7a99c4414f4aaf210243db1aa519'
url='https://api.binance.com/api/v3/order'
payload = {'symbol': 'BTCUSDT', 'orderId':orderId}
payload['signature'] = generate_signature(payload)
payload['Accept'] = 'application/json'
payload['User-Agent'] = 'binance/python'
payload['X-MBX-APIKEY'] = para[1]
ret = requests.delete(url, data=payload)

#综上，必须用session对象才能进行有签名的操作，session对象是必不可少的
#综上，同样的参数，用get方法就是查看该uri下面的资源，用delete方法就是删除该uri下面的资源
