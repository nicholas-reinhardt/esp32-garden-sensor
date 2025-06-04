#pico_blink.py

from machine import Pin
import time

time.sleep(2)

# Set up the onboard LED pin (GP25 on the Pico)
led = Pin(25, Pin.OUT)

while True:
    led.on()          # Turn the LED on
    time.sleep(1)     # Wait for 1 second
    led.off()         # Turn the LED off
    time.sleep(1)     # Wait for 1 second
