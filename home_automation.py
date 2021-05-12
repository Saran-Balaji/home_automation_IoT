Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from time import sleep
import RPi.GPIO as GPIO
from gpiozero import LED
from gpiozero import MCP3008
import time
import requests

light = LED(27)
fan = LED(5)
motor = LED(6)


while True:

     
    temp = MCP3008(0)
    Temp = (temp.value * 100) + 18
    print('Temp=' + str(Temp))
    gas = MCP3008(1)
    Gas = gas.value * 10
    print('Gas=' + str(Gas))
    lvl = MCP3008(2)
    Lvl = lvl.value * 10
    print('Lvl=' + str(Lvl))
    sleep(1)

    #r =requests.get('http://www.iotclouddata.com/20log/012/iot20.php?A=Gas=' + str(gas.value))
    if Temp > 29:
        print('High Temperature')
        r =requests.get('http://www.iotclouddata.com/20log/292/iot20.php?A=Alert_High_Temperature')
    if Gas > 4:
        print('Gas Detected')
        r =requests.get('http://www.iotclouddata.com/20log/292/iot20.php?A=Alert_Gas_detected')

    if Lvl > 3:
        print('High water level')
        r =requests.get('http://www.iotclouddata.com/20log/292/iot20.php?A=Alert_High_water_level_detected')
        
    r =requests.get('http://www.iotclouddata.com/20log/292/getstatus.php')
    print(r.text[7])
    print(r.text[8])
    print(r.text[9])
    print(r.text[10])

    if int(r.text[7]) == 1:
        light.on()
    else:
        light.off()

    if int(r.text[8]) == 1:
        fan.on()
    else:
        fan.off()
    if int(r.text[9]) == 1:
        motor.on()
    else:
        motor.off()




        
    

