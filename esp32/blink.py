import time
import machine
import neopixel

# Setup
pin = 8  # GPIO8
n = 1    # Number of LEDs
np = neopixel.NeoPixel(machine.Pin(pin), n)

# Blink loop
while True:
    np[0] = (255, 0, 0)  # Red
    np.write()
    time.sleep(0.5)

    np[0] = (0, 0, 0)    # Off
    np.write()
    time.sleep(0.5)
