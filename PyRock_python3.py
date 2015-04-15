import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
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
            data = urllib.parse.urlencode(values)
            req = urllib.request.Request(url, data)
            response = urllib.request.urlopen(req)
            strBalance = response.readall().decode('utf-8')
            Balance = json.loads(strBalance)
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
            data = urllib.parse.urlencode(values)
            req = urllib.request.Request(url, data)
            response = urllib.request.urlopen(req)
            strOrders = response.readall().decode('utf-8')
            Orders = json.loads(strOrders)
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
            data = urllib.parse.urlencode(values)
            req = urllib.request.Request(url, data)
            response = urllib.request.urlopen(req)
            strBuyOrder = response.readall().decode('utf-8')
            BuyOrder = json.loads(strBuyOrder)
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
            data = urllib.parse.urlencode(values)
            req = urllib.request.Request(url, data)
            response = urllib.request.urlopen(req)
            strSellOrder = response.readall().decode('utf-8')
            SellOrder = json.loads(strSellOrder)
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
            data = urllib.parse.urlencode(values)
            req = urllib.request.Request(url, data)
            response = urllib.request.urlopen(req)
            strOrderDeleted = response.readall().decode('utf-8')
            OrderDeleted = json.loads(strOrderDeleted)
            return OrderDeleted
        except:
            return None
    
      # getting ticker for a certain currency / fund
    def MarketData(self, fund):
        self.fund=fund
        Url = "https://www.therocktrading.com/api/ticker/"+self.fund
        ResponseTrt = urllib.request.urlopen(Url)
        strMkData = ResponseTrt.readall().decode('utf-8')
        MkData = json.loads(strMkData)
        return MkData

      # get all market tickers
    def AllMarketData(self):
        Url = "https://www.therocktrading.com/api/tickers/"
        ResponseTrt = urllib.request.urlopen(Url)
        strAllMkData = ResponseTrt.readall().decode('utf-8')
        AllMkData = json.loads(strAllMkData)
        return AllMkData

      # getting last trades for a fund since a date
    def LastTrades(self, fund, date):
        self.date = date
        self.fund = fund
        Url = "https://www.therocktrading.com/api/trades/"+self.fund+"/?since="+self.date
        ResponseTrt = urllib.request.urlopen(Url)
        strTrades = ResponseTrt.readall().decode('utf-8')
        Trades = json.loads(strTrades)
        return Trades

      # getting the full orderbook
    def OrderBook(self, fund):
        self.fund=fund
        Url = "https://www.therocktrading.com/api/orderbook/"+self.fund
        ResponseTrt = urllib.request.urlopen(Url)
        strOrders = ResponseTrt.readall().decode('utf-8')
        Orders = json.loads(strOrders)
        return Orders
