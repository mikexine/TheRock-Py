#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
import pusherclient #live stream client: https://github.com/ekulyk/PythonPusherClient
import logging
import time


def trade_callback(data): #some callbacs to do something when the event occours
    print "trade", data

def order_deleted_callback(data):
    print "delete", data

def order_created_callback(data):
    print "create", data

def order_changed_callback(data):
    print "changes", data
    
def order_book_callback(data):
    print "book", data

def connect_handler(data): #this gets called when the Pusher connection is established
    trades_channel = pusher.subscribe("live_trades")
    trades_channel.bind('trade', trade_callback)

    order_book_channel = pusher.subscribe('order_book');
    order_book_channel.bind('data', order_book_callback)

    orders_channel = pusher.subscribe("live_orders")
    orders_channel.bind('order_deleted', order_deleted_callback)
    orders_channel.bind('order_created', order_created_callback)
    orders_channel.bind('order_changed', order_changed_callback)


if __name__ == '__main__': #this is the main() function
    pusher = pusherclient.Pusher("de504dc5763aeef9ff52")
    # pusher.connection.logger.setLevel(logging.WARNING) #no need for this line if you want everything printed out by the logger
    pusher.connection.bind('pusher:connection_established', connect_handler)
    pusher.connect()

    while True:  #run until ctrl+c interrupts
        time.sleep(1)