import machine
import time

time.sleep(2)

led = machine.Pin(1, machine.Pin.OUT)  # GPIO2 is usually the onboard LED

for i in range(10):
    led.value(not led.value())  # Toggle LED
    time.sleep(0.5)             # Delay 500ms
    