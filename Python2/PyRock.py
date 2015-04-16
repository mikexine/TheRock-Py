import json
import requests

class PyRock:
    
      # credentials
    def __init__(self, Username, Password, ApiKey):
        self.username=Username
        self.password=Password
        self.key = ApiKey

      # get the balance for a certain currency 
    def GetBalance(self, currency):
        try:
            currency = currency.upper()
            url = 'https://www.therocktrading.com/api/get_balance'
            values = {
            'username' : self.username,
            'password' : self.password,
            'api_key'  : self.key,
            'type_of_currency' : currency
            }
            headers = {'content-type': 'application/json'}
            r = requests.post(url, data=json.dumps(values), headers = headers)
            return r.json()
        except:
            return None

      # get discount level for a certain currency
    def GetDiscountLevel(self, currency):
        try:
            currency = currency.upper()
            url = 'https://www.therocktrading.com/api/get_discountlevel'
            values = {
            'username' : self.username,
            'password' : self.password,
            'api_key'  : self.key,
            'type_of_currency' : currency
            }
            headers = {'content-type': 'application/json'}
            r = requests.post(url, data = json.dumps(values), headers = headers)
            return r.json()
        except:
            return None


      # get the list of active orders for the account 
    def GetOrders(self):
        try:
            url = 'https://www.therocktrading.com/api/get_orders'
            values = {
            'username' : self.username,
            'password' : self.password,
            'api_key'  : self.key
            }
            headers = {'content-type': 'application/json'}
            r = requests.post(url, data = json.dumps(values), headers = headers)
            return r.json()
        except:
            return None

      # placing a buy order
    def PlaceBuyOrder(self, fund, amount, price):
        try:
            fund = fund.upper()
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
            headers = {'content-type': 'application/json'}
            r = requests.post(url, data = json.dumps(values), headers = headers)
            return r.json()
        except:
            return None

      # placing a sell order
    def PlaceSellOrder(self, fund, amount, price):
        try:
            fund = fund.upper()
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
            headers = {'content-type': 'application/json'}
            r = requests.post(url, data = json.dumps(values), headers = headers)
            return r.json()
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
            headers = {'content-type': 'application/json'}
            r = requests.post(url, data = json.dumps(values), headers = headers)
            return r.json()
        except:
            return None
    
      # getting ticker for a certain currency / fund
    def MarketData(self, fund):
        self.fund = fund.upper()
        url = "https://www.therocktrading.com/api/ticker/"+self.fund
        headers = {'content-type': 'application/json'}
        r = requests.get(url, headers = headers)
        return r.json()

      # get all market tickers
    def AllMarketData(self):
        url = "https://www.therocktrading.com/api/tickers/"
        headers = {'content-type': 'application/json'}
        r = requests.get(url, headers = headers)
        return r.json()

      # getting last trades for a fund since a date
    def LastTrades(self, fund, date):
        self.date = date
        self.fund = fund.upper()
        url = "https://www.therocktrading.com/api/trades/"+self.fund+"/?since="+self.date
        headers = {'content-type': 'application/json'}
        r = requests.get(url, headers = headers)
        return r.json()

      # getting the full orderbook
    def OrderBook(self, fund):
        self.fund=fund.upper()
        url = "https://www.therocktrading.com/api/orderbook/"+self.fund
        headers = {'content-type': 'application/json'}
        r = requests.get(url, headers = headers)
        return r.json()
