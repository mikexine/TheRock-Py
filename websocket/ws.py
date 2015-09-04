
import sys
import pusherclient
import time

# Add a logging handler so we can see the raw communication data
import logging
root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
root.addHandler(ch)

global pusher

# We can't subscribe until we've connected, so we use a callback handler
# to subscribe when able
def connect_handler(data):
    channel = pusher.subscribe('BTCEUR')
    channel.bind('orderbook_diff', callback)

pusher = pusherclient.Pusher('8458eb6fbd288f0cf3d8')
pusher.connection.bind('pusher:connection_established', connect_handler)
pusher.connect()


while True:
    time.sleep(1)