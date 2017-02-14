#!/usr/bin/env python
import grovepi
import math
import dweepy
import time

temp_hum_sensor = 7 # for Temperature & Humidity Sensor
light_sensor = 0 # for Light Sensor

grovepi.pinMode(light_sensor,"INPUT") # light sensor
while True:
    try:
        # For temp & hum, starts
        [temp,humidity] = grovepi.dht(temp_hum_sensor,0)
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temperature = %.02f C humidity =%.02f%%"%(temp, humidity))
            dweepy.dweet_for('cba-hk-iot',{'temperature':temp,'humidity':humidity})
        time.sleep(.01)
        # For temp & hum, ends
        
        # For light, starts
        light_sensor_value = grovepi.analogRead(light_sensor)
        print("sensor_value = %d " %(light_sensor_value))
        dweepy.dweet_for('cba-hk-iot-light',{'light':light_sensor_value})
        time.sleep(.01)
        # For light, ends

    except IOError:
        print ("Error")
