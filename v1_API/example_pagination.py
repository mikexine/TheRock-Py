# be careful! You can't run this script as it is, because you must respect the 5-calls-per-second limit on therocktrading.com

from PyRock import PyRock
import sys

# redirect print output to a text file

sys.stdout = open("./test.txt", "w")

# Insert your APIKEY and you APISECRET here. You can also skip this and leave 'INSERT_KEY' and 'INSERT_SECRET' if 
# you don't need authenticated requests. 

apikey = 'INSERT_KEY'
apisecret = 'INSERT_SECRET'
rock = PyRock(apikey, apisecret)

# example of pagination for all trades of BTCEUR, be careful, you should remember that the limit for API calls is 5 requests per second. 
# use rock.paginate: it will make an unauthenticated GET request to an URL that you pass to it
trades = rock.Trades('btceur')
tradelist = trades['trades']
currenturl = trades['meta']['current']['href']
print 'current '+currenturl
nexturl = trades['meta']['next']['href']
print 'nexturl '+nexturl
lasturl = trades['meta']['last']['href']
print 'lasturl '+lasturl

while currenturl != lasturl: 
	moretrades = rock.paginate(nexturl)
	currenturl = moretrades['meta']['current']['href']
	print 'current '+currenturl
	try:
		nexturl = moretrades['meta']['next']['href']
	except:
		pass
	print 'nexturl '+nexturl
	tradelist = tradelist + moretrades['trades']

print tradelist

# example of pagination for all USER trades of BTCEUR, be careful, you should remember that the limit for API calls is 5 requests per second. 
# To do this you must be authenticated, and you have to use rock.paginateSIG: it will make an authenticated GET request to an URL that you pass to it

trades = rock.UserTrades('btceur')
tradelist = trades['trades']
currenturl = trades['meta']['current']['href']
print 'current '+currenturl
nexturl = trades['meta']['next']['href']
print 'nexturl '+nexturl
lasturl = trades['meta']['last']['href']
print 'lasturl '+lasturl

while currenturl != lasturl: 
	moretrades = rock.paginateSig(nexturl)
	currenturl = moretrades['meta']['current']['href']
	print 'current '+currenturl
	try:
		nexturl = moretrades['meta']['next']['href']
	except:
		pass
	print 'nexturl '+nexturl
	tradelist = tradelist + moretrades['trades']

print tradelist
