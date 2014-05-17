from PyRock import PyRock

rock = PyRock('mykey','mysecretkey')

# asking TheRock for the data of the fund 'btceur' 
#(this is BTC/EUR, it may be any other listed on TRT)

Data = rock.MarketData('btceur')
print Data
print ''

# asking the rock for the trades of the 'eurdog' fund since 1398010268
# (this is EUR/DOGE trades, since 1398010268; date expressed in UnixTime)
trades = rock.LastTrades('eurdog', '1398010268')
print trades
print ''

# asking the rock for the OrderBook of the 'btcusd' fund
# (this is BTC/USD, it provides both bids and asks)
orders = rock.OrderBook('btcusd')
print orders
print ''
