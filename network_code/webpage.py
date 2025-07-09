import network
import socket
import time

# Home Wi-Fi credentials
SSID = 'YOUR_WIFI_NAME'
PASSWORD = 'YOUR_WIFI_PASSWORD'

# Static IP config
STATIC_IP = '192.168.1.123'  # Make sure this is unused on your network
SUBNET_MASK = '255.255.255.0'
GATEWAY = '192.168.1.1'
DNS = '8.8.8.8'

# Connect to Wi-Fi with static IP
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.ifconfig((STATIC_IP, SUBNET_MASK, GATEWAY, DNS))
wlan.connect(SSID, PASSWORD)

# Wait until connected
while not wlan.isconnected():
    time.sleep(1)

print('Connected to Wi-Fi')
print('ESP32 IP:', wlan.ifconfig()[0])

# HTML page to serve
html = """<!DOCTYPE html>
<html>
<head><title>ESP32 Garden</title></head>
<body>
    <h1>Garden Sensor</h1>
    <p>Everything's working fine 🌱</p>
</body>
</html>
"""

# Start socket server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('Listening on', addr)

while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    conn.recv(1024)
    conn.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
    conn.send(html)
    conn.close()
