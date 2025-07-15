#import machine and time libraries
from machine import Pin, ADC
import time


#setup adc pin
'''
Note:
    The esp32c3-devkitM1 expects a voltage range between 0v and 1.1v by default,
    This means that you must attenuate the input voltage to get the correct range from the soil moisture sensor
    in this case, 11dB comes out to a max range of 2.45v of readable voltage
    absolute max input voltage to the analog pin without damage is 3.7v
    consult the docs for your board if you're using something else.
'''
adc_pin = ADC(Pin(0))
adc_pin.atten(ADC.ATTN_11DB)


#measure dry and wet values and record as the max and min
'''
Note:
    unintuitively, this means dry is more voltage, wet is less voltage
    when I measured mine with adc_pin.read(), I got 3000 dry, and 1000 wet
'''
dry = 3000
wet = 1000


#measure analog reading
while True:
    soil_volts = adc_pin.read()
    if (soil_volts < wet):
        print("Soil Moisture: 100\%")
    elif (soil_volts > dry):
        print("Soil Moisture: 0%")
    else:
        moisture = (soil_volts - dry) * 100 / (wet - dry)
        print("Soil Moisture: %i%%" % moisture)
    time.sleep(0.5)