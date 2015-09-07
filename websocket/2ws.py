#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
import pusherclient #live stream client: https://github.com/ekulyk/PythonPusherClient
import logging
import time
import json


def orderbook_diff_callback(data): #some callbacs to do something when the event occours
    prova = json.loads(data)
    print "change in orderbook: "
    print prova['side']
    print prova['price']
    print prova['amount']

def connect_handler(data): #this gets called when the Pusher connection is established
    trades_channel = pusher.subscribe('BTCEUR')
    trades_channel.bind('orderbook_diff', orderbook_diff_callback)


    # order_book_channel.bind('orderbook_diff', order_book_callback)

    # orders_channel.bind('new_offer', order_deleted_callback)
    # orders_channel.bind('order_created', order_created_callback)
    # orders_channel.bind('order_changed', order_changed_callback)


if __name__ == '__main__': #this is the main() function
    pusher = pusherclient.Pusher("8458eb6fbd288f0cf3d8")
    # pusher.connection.logger.setLevel(logging.WARNING) #no need for this line if you want everything printed out by the logger
    pusher.connection.bind('pusher:connection_established', connect_handler)
    pusher.connect()

    while True:  #run until ctrl+c interrupts
        time.sleep(1)