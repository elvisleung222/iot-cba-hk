#!/usr/bin/env python
import grovepi
import math
import dweepy
import time
from datetime import timedelta

from grove_rgb_lcd import * # for Grove-LCD RGB Backlight

temp_hum_sensor = 7 # for Temperature & Humidity Sensor
light_sensor = 0 # for Light Sensor

temp_threshold = 20 # celsius degree
hum_threshold = 30 # percentage
light_threshold = 500 # general unit

grovepi.pinMode(light_sensor,"INPUT") # light sensor

# testing
# setText("Hello world\nLCD test")
# setRGB(0,128,64)

# Slowly change the colors every 0.01 seconds.

# testing
def lightOn():
    setText("UV light On")
    setRGB(0,255,0)
    return

def lightOff():
    setText("UV light Off")
    setRGB(0,0,0)
    return

startTime = time.time()
naturalLight = 0
extraLight = 0

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
        time.sleep(1)
        light_sensor_value = grovepi.analogRead(light_sensor)
        print("sensor_value = %d " %(light_sensor_value))
        light_alert = 0
        if light_sensor_value < light_threshold:
            light_alert = 1 #to turn on the light alert
            lightOn()
        else:
            lightOff()
        # Getting value light, ends
        # Counting time
        nowTime = time.time()
        td = timedelta(seconds = int(nowTime - startTime))
        # Sending out data, starts
        naturalLight = naturalLight + int(light_sensor_value) * int(td.seconds)
        dweepy.dweet_for('cba-hk-iot',{
            'time_fried':str(td),
            'natural_sunlight_exposure':naturalLight,
            'extra_sunlight_exposure':1,
            'temperature':temp,
            'temp_alert':temp_alert,
            'humidity':humidity,
            'hum_alert':hum_alert,
            'light':light_sensor_value,
            'light_alert':light_alert})
        # Sending out data, ends
        time.sleep(1)
    except Exception as e:
        print ("Error: ",str(e))
        pass
