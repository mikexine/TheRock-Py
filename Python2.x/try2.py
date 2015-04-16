from PyRock import PyRock
from time import sleep

## this is just an example. if you want to run it, you need to insert
## your username, password and API key - you can generate one in your 
## personal page on The Rock.
##
## Note that MarketData, AllMarketData, LastTrades and GetBalance functions
## do NOT require an API KEY 
##
## I put a sleep(1) between each query because The Rock has a request limit
## which is five API calls per second. This is just an example, so there's
## no need to be fast. 
##
## You should have a look on the code before putting in it your account
## data and running it. This one creates also some orders, so you might
## check them before they are created. Also, there might be some bug or
## error, so use this with caution.
##
## Do whatever you want with this code - but keep in mind that I do NOT
## take any responsibility for errors or losses caused by this script.


rock = PyRock('INSERT_USERNAME','INSERT_PASSWORD', 'INSERT_API_KEY')

## asking TheRock for the data of the fund 'btceur' 
## (this is BTC/EUR, it may be any other listed on TRT)
Data = rock.MarketData('btceur')
print Data
print ''
sleep(1)

## asking TheRock for all market tickers
AllData = rock.AllMarketData()
print AllData
print ''
sleep(1)

## asking the rock for the trades of the 'eurdog' fund since 1400284800
## (this is EUR/DOGE trades, since 1400284800; date expressed in UnixTime)
Trades = rock.LastTrades('eurdog', '1400284800')
print Trades
print ''
sleep(1)

## asking the rock for the OrderBook of the 'btcusd' fund
## (this is BTC/USD, it provides both bids and asks)
FullOrderBook = rock.OrderBook('btcusd')
print FullOrderBook
print ''
sleep(1)

## asking the rock for my available balance of a specified currency
## in this case the currency is Ripple
MyBalance = rock.GetBalance('xrp')
print MyBalance
print ''
sleep(1)

## asking the rock for all my open orders
MyOrders = rock.GetOrders()
print MyOrders
print ''
sleep(1)

## placing a buy order for 1 euro at 2 doge
PlaceBuy = rock.PlaceBuyOrder('eurdog', '1', '2')
print PlaceBuy
print ''
sleep(1)

## placing a sell order for 1 btc at 500 eur
PlaceSell = rock.PlaceSellOrder('btceur', '1', '500')
print PlaceSell
print ''
sleep(1)

## cancelling an order with the specified order_id
CancelIt = rock.CancelOrder('1647754')
print CancelIt
print ''
sleep(1)

## getting the Discount Level for Ripple
EurDiscount = rock.GetDiscountLevel('xrp')
print EurDiscount
print ''
sleep(1)
