import json
import requests
import hmac
import hashlib
import time

StdUrl = 'https://api.therocktrading.com/v1/'

class PyRock:
    
      # credentials
    def __init__(self, ApiKey, Secret):
        self.key = ApiKey
        self.secret = Secret

      # create headers
    @classmethod
    def getheaders(self, url, secret, key):
        nonce = str(int(time.time() * 1e6))
        message = str(nonce)+url
        signature = hmac.new(secret, msg=message, digestmod=hashlib.sha512).hexdigest()
        headers = {'content-type': 'application/json', 'X-TRT-KEY': key, 'X-TRT-SIGN': signature, 'X-TRT-NONCE': nonce}
        return headers

# BASIC API https://api.therocktrading.com/doc/v1/#api-Basic_API

      # Balance of a certain fund
    def Balance(self, fund):
        url = StdUrl+'balances/'+fund.upper()
        r = requests.get(url, headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

      # All Balances
    def AllBalances(self):
        url = StdUrl+'balances'
        r = requests.get(url, headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

      # discount levels of one fund
    def DiscountLevel(self, fund):
        url = StdUrl+'discounts/'+fund.upper()
        r = requests.get(url, headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

      # discount levels of all funds
    def AllDiscountLevels(self):
        url = StdUrl+'discounts'
        r = requests.get(url, headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

      #Withdraw limits of one fund
    def WithdrawLimit(self, fund):
        url = StdUrl+'withdraw_limits/'+fund.upper()
        r = requests.get(url, headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

      #Withdraw limits of all funds
    def AllWithdrawLimits(self):
        url = StdUrl+'withdraw_limits'
        r = requests.get(url, headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()


# MARKET API https://api.therocktrading.com/doc/v1/#api-Market_API
    
      # get all funds at once
    def Funds(self):
        url = StdUrl+'funds'
        r = requests.get(url, headers = {'content-type': 'application/json'})
        return r.json()
    
      # get the orderbook for a certain fund
    def OrderBook(self, fund):
        url = StdUrl+'funds/'+fund.upper()+'/orderbook'
        r = requests.get(url, headers = {'content-type': 'application/json'})
        return r.json()

      # get the ticker for a certain fund
    def Ticker(self, fund):
        url = StdUrl+'funds/'+fund.upper()+'/ticker'
        r = requests.get(url, headers = {'content-type': 'application/json'})
        return r.json()

      # get all tickers
    def AllTickers(self):
        url = StdUrl+'funds/tickers'
        r = requests.get(url, headers = {'content-type': 'application/json'})
        return r.json()

      # get the last trades for a certain fund, with pagination. 
    def Trades(self, fund):
        url = StdUrl+'funds/'+fund.upper()+'/trades'
        r = requests.get(url, headers = {'content-type': 'application/json'})
        return r.json()

      # get the last trades for a certain fund, after x date and before x date, with pagination
    def TradesTime(self, fund, after, before):
        url = StdUrl+'funds/'+fund.upper()+'/trades?after='+after+'&before='+before
        r = requests.get(url, headers = {'content-type': 'application/json'})
        return r.json()


# TRADING API https://api.therocktrading.com/doc/v1/#api-Trading_API

      # Show the list of orders for a certain fund
    def ListAllOrders(self, fund):
        url = StdUrl+'funds/'+fund.upper()+'/orders'
        r = requests.get(url, headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

      # Show the details of one order
    def ListOrder(self, fund, orderId):
        url = StdUrl+'funds/'+fund.upper()+'/orders/'+str(orderId)
        r = requests.get(url, headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

      # Cancell all open orders for a certain fund
    def CancelAllOrders(self, fund):
        url = StdUrl+'funds/'+fund.upper()+'/orders/remove_all'
        r = requests.delete(url, headers = PyRock.getheaders(url, self.secret, self.key))
        return r

      # Show the details of one order
    def CancelOrder(self, fund, orderId):
        url = StdUrl+'funds/'+fund.upper()+'/orders/'+str(orderId)
        r = requests.delete(url, headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

    def PlaceBuyOrder(self, fund, amount, price):
        url = StdUrl+'funds/'+fund.upper()+'/orders'
        values = { 
        'fund_id' : fund.upper(),
        'side' : 'buy',
        'amount' : str(amount),
        'price' : str(price)
        }
        r = requests.post(url, data = json.dumps(values), headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

    def PlaceSellOrder(self, fund, amount, price):
        url = StdUrl+'funds/'+fund.upper()+'/orders'
        values = { 
        'fund_id' : fund.upper(),
        'side' : 'sell',
        'amount' : amount,
        'price' : price
        }
        r = requests.post(url, data = json.dumps(values), headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

      # Get user's transactions, with pagination
    def Transactions(self):
        url = StdUrl+'transactions'
        r = requests.get(url, headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

      # Get user's transactions by FUND_ID, with pagination
    def TransactionsByFund(self, fund):
        url = StdUrl+'transactions?fund_id='+fund.upper()
        callurl = StdUrl+'transactions'
        r = requests.get(url, headers = PyRock.getheaders(callurl, self.secret, self.key))
        return r.json()

      # Get user's transactions by CURRENCY, with pagination
    def TransactionsByCurrency(self, currency):
        url = StdUrl+'transactions?currency='+currency.upper()
        callurl = StdUrl+'transactions'
        r = requests.get(url, headers = PyRock.getheaders(callurl, self.secret, self.key))
        return r.json()

      # Get user's transactions by TIME, with pagination
    def TransactionsByTime(self, after, before):
        url = StdUrl+'transactions?after='+after+'&before='+before
        callurl = StdUrl+'transactions'
        r = requests.get(url, headers = PyRock.getheaders(callurl, self.secret, self.key))
        return r.json()

      # get user's trades only, with pagination 
    def UserTrades(self, fund):
        url = StdUrl+'funds/'+fund.upper()+'/trades'
        r = requests.get(url, headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

      # get user's trades only, with pagination, after a certain date and before another one
    def UserTradesTime(self, fund, after, before):
        url = StdUrl+'funds/'+fund.upper()+'/trades?after='+after+'&before='+before
        r = requests.get(url, headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()


# WITHDRAWAL API https://api.therocktrading.com/doc/v1/#api-Withdrawal_API

      # withdraw a certain currency to an address
    def Withdraw(self, currency, address, amount):
        url = StdUrl+'atms/withdraw'
        values = { 
        'currency' : currency,
        'destination_address' : address,
        'amount' : amount,
        }
        r = requests.post(url, data = json.dumps(values), headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

    def WithdrawRipple(self, currency, address, amount):
        url = StdUrl+'atms/withdraw'
        values = { 
        'currency' : currency.upper(),
        'withdraw_method' : 'RIPPLE',
        'destination_address' : address,
        'amount' : amount
        }
        r = requests.post(url, data = json.dumps(values), headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

      # authenticated GET request to one url, used in example_pagination.py
    def paginateSig(self, url):
        r = requests.get(url, headers = PyRock.getheaders(url, self.secret, self.key))
        return r.json()

      # unauthenticated GET request to one url, used in example_pagination.py
    def paginate(self, url):
        r = requests.get(url, headers = {'content-type': 'application/json'})
        return r.json()
