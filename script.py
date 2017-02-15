#!/usr/bin/env python
import grovepi
import math
import dweepy
import time

temp_hum_sensor = 7 # for Temperature & Humidity Sensor
light_sensor = 0 # for Light Sensor

temp_threshold = 20
hum_threshold = 30
light_threshold = 500

grovepi.pinMode(light_sensor,"INPUT") # light sensor
while True:
    try:
        # Getting value temp & hum , starts
        temp_alert = 0
        hum_alert = 0
        [temp,humidity] = grovepi.dht(temp_hum_sensor,0)
        if temp < temp_threshold:
            temp_alert = 1 #to turn on the temperature alert
        if humidity < hum_threshold:
            hum_alert = 1 #to turn on the humidity alert
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temperature = %.02f C humidity =%.02f%%"%(temp, humidity))
        # Getting value temp & hum, ends

        # Getting value light, starts
        time.sleep(0.7)
        light_sensor_value = grovepi.analogRead(light_sensor)
        print("sensor_value = %d " %(light_sensor_value))
        light_alert = 0
        if light_sensor_value < light_threshold:
            light_alert = 1 #to turn on the light alert
        # Getting value light, ends

        # Sending out data, starts
        dweepy.dweet_for('cba-hk-iot',{
            'temperature':temp,
            'temp_alert':temp_alert,
            'humidity':humidity,
            'hum_alert':hum_alert,
            'light':light_sensor_value,
            'light_alert':light_alert})
        # Sending out data, ends
        time.sleep(.001)
    except IOError:
        print ("Error")
