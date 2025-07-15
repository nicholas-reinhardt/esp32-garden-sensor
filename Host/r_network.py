#this is the reciever network
import network
import espnow
import time

def setup:
    # setup wireless local area network in interface station mode
    print("Setting up Wireless Local Area Network")
    station = network.WLAN(network.WLAN.IF_STA)
    station.active(True)
    time.sleep(1)

    print("Setting up ESPNOW communications")
    ESPNOW = espnow.ESPNow()
    ESPNOW.active(True)


#wait for messages
while True:
    host, msg = ESPNOW.recv()
    if msg:             # msg == None if timeout in recv()
        print(host, msg)
        if msg == b'end':
            break
