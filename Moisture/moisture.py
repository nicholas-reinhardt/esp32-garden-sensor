'''
pin 0 is the data from the soil moisture sensor
MUST use voltage divider to take down the 3.3v output from the
moisture sensor down to 1.1v max

contact with the soil is important for accurate readings

you should recalibrate the dry and wet values to get proper percentages
'''

from machine import ADC, Pin


#define pin and calibrate sensor
moisture = ADC(Pin(0))
dry = 26070
wet = 700


#read raw, scale, and map
raw = moisture.read_u16()
moisture_percent = (dry - raw) * 100 // (dry - wet)
moisture_percent = max(0, min(100, moisture_percent))

#uncomment this to calibrate dry and wet
#print(raw)

print(f"Moisture: {moisture_percent}%")