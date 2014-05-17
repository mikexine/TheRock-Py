import pycurl
import time
import hmac
import hashlib
import urllib
import StringIO
import json

class PyRock:
    

      # get keys (this part is not complete)
    def __init__(self, Key, SecretKey):
        self.key=Key
        self.secret=SecretKey
    
    # getting ticker for a certain currency / fund
    def MarketData(self, fund):
        self.fund=fund
        Url = "https://www.therocktrading.com/api/ticker/"+self.fund
        ResponseTrt = urllib.urlopen(Url)
        MkData = json.loads(ResponseTrt.read())
        return MkData

    # getting last trades for a fund since a date
    def LastTrades(self, fund, date):
        self.date = date
        self.fund = fund
        Url = "https://www.therocktrading.com/api/trades/"+self.fund+"/?since="+self.date
        ResponseTrt = urllib.urlopen(Url)
        Trades = json.loads(ResponseTrt.read())
        return Trades

    def OrderBook(self, fund):
        self.fund=fund
        Url = "https://www.therocktrading.com/api/orderbook/"+self.fund
        ResponseTrt = urllib.urlopen(Url)
        Orders = json.loads(ResponseTrt.read())
        return Orders
