from PyRock import PyRock
from time import sleep 
import sys

# Insert your APIKEY and you APISECRET here. You can also skip this and leave 'INSERT_KEY' and 'INSERT_SECRET' if 
# you don't need authenticated requests. 

apikey = 'API_KEY'
apisecret = 'API_SECRET'

rock = PyRock(apikey, apisecret)

# This is just a small example. Be careful, I am not responsible if something doesn't work correctly. I put sleep(1) after 
# every API call to avoid rate limiting (you can do up to 5 calls per second)

# redirect all print(something) to a text file
sys.stdout = open("./test.txt", "w")

# BASIC API https://api.therocktrading.com/doc/v1/#api-Basic_API

# Ask the balance of one fund of your account
balance = rock.Balance('eur')
print(balance)
print('')
sleep(1)

# Ask the balance of all funds of your account
balances = rock.AllBalances()
print(balances)
print('')
sleep(1)

# Ask the discount levels of one fund of your account
disclevel = rock.DiscountLevel('eur')
print(disclevel)
print('')
sleep(1)

# Ask the discount levels of all funds of your account
disclevels = rock.AllDiscountLevels()
print(disclevels)
print('')
sleep(1)

# Ask the withdraw limits of one fund of your account
withlimit = rock.WithdrawLimit('btc')
print(withlimit)
print('')
sleep(1)

# Ask the withdraw limits of all funds of your account
withlimits = rock.AllWithdrawLimits()
print(withlimits)
print('')
sleep(1)


# MARKET API https://api.therocktrading.com/doc/v1/#api-Market_API

# Returns the available funds on The Rock
funds = rock.Funds()
print(funds)
print('')
sleep(1)

# Returns the whole orderbook for one fund
orderbook = rock.OrderBook('btceur')
print(orderbook)
print('')
sleep(1)

# Returns the ticker for one fund
ticker = rock.Ticker('ltcbtc')
print(ticker)
print('')
sleep(1)

# Returns all tickers
tickers = rock.AllTickers()
print(tickers)
print('')
sleep(1)

# Returns all trades for one fund. Have a look at the examples, it uses pagination
trades = rock.Trades('btceur')
print(trades)
print('')
sleep(1)

# Returns all trades for one fund in a certain timespan. Have a look at the examples, it uses pagination
after = '2014-06-01'
before = '2014-07-01'
tradestime = rock.TradesTime('btceur', after, before)
print(tradestime)
print('')
sleep(1)

# TRADING API https://api.therocktrading.com/doc/v1/#api-Trading_API

# List the details of all your open orders for one fund
orders = rock.ListAllOrders('eurdog')
print(orders)
print('')
sleep(1)

# List the details of one order
orderid = 20651258
orders = rock.ListOrder('eurdog', orderid)
print(orders)
print('')
sleep(1)

# Cancel all your open orders for one fund
orders = rock.CancelAllOrders('eurdog')
print(orders)
print('')
sleep(1)

# Cancel one order
orderid = 20474758
orders = rock.CancelOrder('eurdog', orderid)
print(orders)
print('')
sleep(1)

# Place a buy order (example: buy 1 euro at 1 dogecoin)
fund = 'eurdog'
amount = 1
price = 1
buyorder = rock.PlaceBuyOrder(fund, amount, price)
print(buyorder)
print('')
sleep(1)

# Place a sell order (example: sell 0.01 euro at 5000000000 dogecoin)
fund = 'eurdog'
amount = 0.01
price = 5000000000
sellorder = rock.PlaceSellOrder(fund, amount, price)
print(sellorder)
print('')
sleep(1)

# Get my transactions
txs = rock.Transactions()
print(txs)
print('')
sleep(1)

# Get my transactions for one fund
txsfund = rock.TransactionsByFund('btceur')
print(txsfund)
print('')
sleep(1)

# Get my transactions for one currency
txsfund = rock.TransactionsByCurrency('LTC')
print(txsfund)
print('')
sleep(1)

# Get my transactions in a certain timespan
after = '2014-06-01'
before = '2014-07-01'
txstime = rock.TransactionsByTime(after, before)
print(txstime)
print('')
sleep(1)

# Get my trades
tradx = rock.UserTrades('btceur')
print(tradx)
print('')
sleep(1)

# Get my trades in a certain timespan
after = '2014-06-01'
before = '2014-07-01'
tradx = rock.UserTradesTime('btceur', after, before)
print(tradx)
print('')
sleep(1)


# WITHDRAWAL API https://api.therocktrading.com/doc/v1/#api-Withdrawal_API

# Withdraw one doge to DANU5x3vECGwUVnwBSjm9gAu1qTJBPHiJk
curr = 'DOGE'
add = 'doge'
am = 1000
withd = rock.Withdraw(curr, add, am)
print(withd)

# # Withdraw 5 euro to a ripple address
currency = 'XRP'
rippleaddress = 'ripple'
amount = 3
withdrawR = rock.WithdrawRipple(currency, rippleaddress, amount)
print(withdrawR)
