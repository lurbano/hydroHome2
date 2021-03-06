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

flowrate=15

t=.75
for j in range(5):
    for i in range(20):
        rval=i**1.7
        bval=255-i**1.7
        pixels[i] = (0,rval,bval)
        time.sleep(t)
        pixels[i] = (0,0,0)
    for i in range(19,-1,-1):
        t2= (5/(i+1))/12
        bval=i**1.7
        rval=255-i**1.7
        pixels[i] = (0,-rval+255,-bval+255)
        time.sleep(t2)
        pixels[i] = (0,0,0)
