import urllib
import urllib2
import json

class PyRock:
    
      # get keys unixtime today
    def __init__(self, Username, Password, ApiKey):
        self.username=Username
        self.password=Password
        self.key = ApiKey

      # get the balance for a certain currency (return None if not found)
    def GetBalance(self, currency):
        try:
            url = 'https://www.therocktrading.com/api/get_balance'
            values = {
            'username' : self.username,
            'password' : self.password,
            'api_key'  : self.key,
            'type_of_currency' : currency
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            Balance = json.loads(response.read())
            return Balance
        except:
            return None

      # get the list of orders active for the account (return None if not found)
    def GetOrders(self):
        try:
            url = 'https://www.therocktrading.com/api/get_orders'
            values = {
            'username' : self.username,
            'password' : self.password,
            'api_key'  : self.key
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            Orders = json.loads(response.read())
            return Orders
        except:
            return None

      # placing a buy order
    def PlaceBuyOrder(self, fund, amount, price):
        try:
            url = 'https://www.therocktrading.com/api/place_order'
            values = {
            'username'   : self.username,
            'password'   : self.password,
            'api_key'    : self.key,
            'fund_name'  : fund,
            'order_type' : 'B',
            'amount'     : amount,
            'price'      : price
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            BuyOrder = json.loads(response.read())
            return BuyOrder
        except:
            return None

      # placing a sell order
    def PlaceSellOrder(self, fund, amount, price):
        try:
            url = 'https://www.therocktrading.com/api/place_order'
            values = {
            'username'   : self.username,
            'password'   : self.password,
            'api_key'    : self.key,
            'fund_name'  : fund,
            'order_type' : 'S',
            'amount'     : amount,
            'price'      : price
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            SellOrder = json.loads(response.read())
            return SellOrder
        except:
            return None

      # cancel a specified order
    def CancelOrder(self, orderid):
        try:
            url = 'https://www.therocktrading.com/api/cancel_order'
            values = {
            'username'   : self.username,
            'password'   : self.password,
            'api_key'    : self.key,
            'order_id'   : orderid
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            OrderDeleted = json.loads(response.read())
            return OrderDeleted
        except:
            return None
    
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

      # getting the full orderbook
    def OrderBook(self, fund):
        self.fund=fund
        Url = "https://www.therocktrading.com/api/orderbook/"+self.fund
        ResponseTrt = urllib.urlopen(Url)
        Orders = json.loads(ResponseTrt.read())
        return Orders
