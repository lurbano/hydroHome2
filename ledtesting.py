import RPi.GPIO as GPIO
import time
import board
import neopixel

#pump stuff
in1 = 16
pumpRate=25
VolNeeded=21000
pumpTime= VolNeeded/pumpRate
secondsneeded=(60*60*24)-pumpTime

#LED stuff
timestorun=4
numpix = 20
t2=.02
pixels = neopixel.NeoPixel(board.D18, numpix)

flowrate=25
for i in range(20):
    rval=i**1.7
    bval=255-i**1.7
    pixels[i] = (rval,0,bval)
    t=flowrate/500
    time.sleep(t)
    pixels[i] = (0,0,0)
time.sleep(t)
for i in range(19,-1,-1):
    bval=i**1.7
    rval=255-i**1.7
    pixels[i] = (rval,0,bval)
    time.sleep(t2)
    pixels[i] = (0,0,0)
time.sleep(t)
