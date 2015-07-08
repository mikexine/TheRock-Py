# example of pagination for all trades of EURDOG, be careful, you should remember that the limit for API calls is 5 requests per second. 
trades = rock.Trades('eurdog')
tradelist = trades['trades']
currenturl = trades['meta']['current']['href']
print 'current '+currenturl
nexturl = trades['meta']['next']['href']
print 'nexturl '+nexturl
lasturl = trades['meta']['last']['href']
print 'lasturl '+lasturl

while currenturl != lasturl: 
	moretrades = rock.MoreTrades(nexturl)
	currenturl = moretrades['meta']['current']['href']
	print 'current '+currenturl
	try:
		nexturl = moretrades['meta']['next']['href']
	except:
		pass
	print 'nexturl '+nexturl
	tradelist = tradelist + moretrades['trades']

print tradelist