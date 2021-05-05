import RPi.GPIO as GPIO
import time
import board
import neopixel

timestorun=4
numpix = 20
t=.03
t2=.05
pixels = neopixel.NeoPixel(board.D18, numpix)


for i in range(20):
    rval=i**1.7
    bval=255-i**1.7
    pixels[i] = (rval,0,bval)
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
