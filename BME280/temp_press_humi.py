#this is the code for the bmp280 on an esp32c3.


#import libraries including drivers for bmp280
import bme280_float as bme280
from machine import Pin, I2C
import time


#setup pins and constants
i2c = I2C(0, scl=Pin(3), sda=Pin(2), freq=100000)
bme = bme280.BME280(i2c=i2c)
bmeVIN = Pin(4, Pin.OUT)
bmeVIN.value(1)

#delay so that I can access interrupt the backend and access REPL if need be
time.sleep(2)


#print bme values
for i in range(10):
    print(f"Temp: {bme.values}")
    time.sleep(1)
    




    #print temps to terminal