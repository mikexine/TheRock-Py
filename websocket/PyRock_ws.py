import pusherclient #install from https://github.com/ekulyk/PythonPusherClient
import time
import json

def new_offer_callback(data):
    new_offers = json.loads(data)
    print 'new offers ', new_offers

def last_trade_callback(data):
    last_trades = json.loads(data)
    print 'last trades ', last_trades

def last_volume_callback(data):
    last_volumes = json.loads(data)
    print 'last volumes ', last_volumes

def orderbook_diff_callback(data): 
    orderbook_diffs = json.loads(data)
    print 'orderbook diffs ', orderbook_diffs

def orderbook_callback(data):
    orderbooks = json.loads(data)
    print 'orderbooks ', orderbooks


def connect_handler(data):
    currency_channel = pusher.subscribe('currency')
    currency_channel.bind('new_offer', new_offer_callback)
    currency_channel.bind('last_trade', last_trade_callback)
    currency_channel.bind('last_volume', last_volume_callback)

    btceur_channel = pusher.subscribe('BTCEUR')
    btceur_channel.bind('orderbook_diff', orderbook_diff_callback)
    btceur_channel.bind('orderbook', orderbook_callback)


if __name__ == '__main__': #this is the main() function
    pusher = pusherclient.Pusher("8458eb6fbd288f0cf3d8")
    pusher.connection.bind('pusher:connection_established', connect_handler)
    pusher.connect()

    while True:  #run until ctrl+c interrupts
        time.sleep(1)