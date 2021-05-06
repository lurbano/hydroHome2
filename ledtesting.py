import RPi.GPIO as GPIO
import time
import board
import neopixel
import math

#pump stuff
in1 = 16
pumpRate=25
VolNeeded=21000
pumpTime= VolNeeded/pumpRate
secondsneeded=(60*60*24)-pumpTime

#LED stuff
timestorun=4
numpix = 20

pixels = neopixel.NeoPixel(board.D18, numpix)

flowrate=25
maxLED= 15
t=.5/flowrate

for i in range(maxLED):
    rval=i**1.7
    bval=255-i**1.7
    pixels[i] = (0,rval,bval)
    time.sleep(t)
    pixels[i] = (0,0,0)
time.sleep(t)
for i in range(maxLED-1,-1,-1):
    t2= (math.log(-i+21))/5
    bval=i**1.7
    rval=255-i**1.7
    pixels[i] = (0,rval,bval)
    time.sleep(t2)
    pixels[i] = (0,0,0)
time.sleep(t)
