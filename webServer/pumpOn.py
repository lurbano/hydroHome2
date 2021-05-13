

import RPi.GPIO as GPIO
import time
import board
import neopixel
import math
import argparse

in1 = 16
pumpRate=25
VolNeeded=21000
pumpTime= VolNeeded/pumpRate
secondsneeded=(60*60*24)-pumpTime


#LED stuff
timestorun=4
numpix = 20
t=.03
t2=.05
pixels = neopixel.NeoPixel(board.D18, numpix)


pumpTime=25

print("pumping for:", pumpTime)
GPIO.output(in1, True)
#LED Pattern while Pumping
startT= time.time()
while elapsedT < pumpTime:

    flowrate=15
    maxLED= int((elapsedT/pumpTime)*20)
    t=.5/flowrate

    for i in range(maxLED):
        rval=i**1.7
        bval=255-i**1.7
        pixels[i] = (0,rval,bval)
        time.sleep(t)
        pixels[i] = (0,0,0)

    for i in range(maxLED-1,-1,-1):
        t2= (5/(i+1))/20
        bval=i**1.7
        rval=255-i**1.7
        pixels[i] = (0,rval,bval)
        time.sleep(t2)
        pixels[i] = (0,0,0)


    endT= time.time()
    elapsedT= endT-startT


GPIO.output(in1, False)
print("Done Pumping")
