from binance_client import *
import time
import hmac
import hashlib
import time
import json, requests


def getSign(data,secret):
    result = hmac.new(secret.encode("utf-8"), data.encode("utf-8"), hashlib.md5).hexdigest()
    return result

def doApiRequestWithApikey(url, cmds, api_key, api_secret):
    r = -1
    try:
        s_cmds = json.dumps(cmds)
        sign = getSign(s_cmds,api_secret)
        r = requests.post(url, data={'cmds': s_cmds, 'apikey': api_key,'sign':sign})
        #print(r.text)
    except Exception:
        print('doApiRequestWithApikey time out', time.time())
        return -1
    if(r.status_code!=200):
        return -1
    return r

def post_trade(api_key,api_secret,cmds):
    url = "https://api.bibox.com/v1/orderpending"
    return doApiRequestWithApikey(url,cmds,api_key,api_secret)

def get_asset_balance(self, asset, **params):
        """Get current asset balance.
        .. code-block:: python
            {
                "asset": "BTC",
                "free": "4723846.89208129",
                "locked": "0.00000000"
            }
        :raises: BinanceRequestException, BinanceAPIException
        """
        res = self.get_account(**params)
        # find asset balance in list of balances
        if "balances" in res:
            for bal in res['balances']:
                if bal['asset'].lower() == asset.lower():
                    return bal
        return None

#from binance_client import *
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

ret = client.order_limit_sell(symbol = 'BNBUSDT', quantity = 1.5, price = '16')#post

ret = client.order_limit_buy(symbol = 'BCCBNB', quantity = '0.025', price = '58')#post


ret = client.get_open_orders(symbol = 'BCCBNB')
orderId = ret[0]['orderId']

