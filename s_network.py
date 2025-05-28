#this is the sender network file
import network
import espnow
import time

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.WLAN.IF_STA)  # Or network.WLAN.IF_AP
sta.active(True)

e = espnow.ESPNow()
e.active(True)
peer = b'\xF0\x9E\x9E\x98\xD2\xD4'   # MAC address of peer's wifi interface
e.add_peer(peer)      # Must add_peer() before send()

e.send(peer, "Starting...")
time.sleep(0.5)
for i in range(10):
    e.send(peer, str(i), True)
    time.sleep(0.5)
e.send(peer, b'end')
