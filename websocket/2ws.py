#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
import pusherclient #live stream client: https://github.com/ekulyk/PythonPusherClient
import logging
import time
import json


def new_offer_callback(d):
    new_offers = json.loads(d)
    print 'new offers ', new_offers

def last_trade_callback(a):
    last_trades = json.loads(a)
    print 'last trades ', last_trades

def orderbook_diff_callback(t): 
    orderbook_diffs = json.loads(t)
    print 'orderbook diffs ', orderbook_diffs

def orderbook_callback(s):
    orderbooks = json.loads(s)
    print 'orderbooks ', orderbooks


def connect_handler(data): #this gets called when the Pusher connection is established
    btceur_channel = pusher.subscribe('BTCEUR')

    btceur_channel.bind('new_offer', new_offer_callback)

    btceur_channel.bind('last_trade', last_trade_callback)

    btceur_channel.bind('orderbook_diff', orderbook_diff_callback)

    btceur_channel.bind('orderbook', orderbook_callback)


if __name__ == '__main__': #this is the main() function
    pusher = pusherclient.Pusher("8458eb6fbd288f0cf3d8")
    # pusher.connection.logger.setLevel(logging.WARNING) #no need for this line if you want everything printed out by the logger
    pusher.connection.bind('pusher:connection_established', connect_handler)
    pusher.connect()

    while True:  #run until ctrl+c interrupts
        time.sleep(1)