#!/usr/bin/env python
import grovepi
import math
import dweepy
import time

temp_hum_sensor = 7 # for Temperature & Humidity Sensor
while True:
    try:
        [temp,humidity] = grovepi.dht(temp_hum_sensor,0)
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temperature = %.02f C humidity =%.02f%%"%(temp, humidity))
            dweepy.dweet_for('cba-hk-iot',{'temperature':temp,'humidity':humidity})
        time.sleep(.01)

    except IOError:
        print ("Error")
