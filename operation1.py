#!/usr/bin/env python
import grovepi
import math
import dweepy
import time
# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
sensor = 7  # The Sensor goes on digital port 4.


# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.


while True:
    try:
        # This example uses the blue colored sensor. 
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = grovepi.dht(sensor,blue)
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temperature = %.02f C humidity =%.02f%%"%(temp, humidity))
            dweepy.dweet_for('cba-hk-iot',{'temperature':temp,'humidity':humidity})
	time.sleep(.01)

    except IOError:
        print ("Error")
