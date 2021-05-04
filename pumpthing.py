import RPi.GPIO as GPIO
import time
import board
import neopixel


#LED stuff
timestorun=4
numpix = 20
t=.03
t2=.05
pixels = neopixel.NeoPixel(board.D18, numpix)

#pump stuff
in1 = 16
pumpRate=25
VolNeeded=21000
pumpTime= VolNeeded/pumpRate
secondsneeded=(60*60*24)-pumpTime
#REMOVE LATER
pumpTime=60*30

elapsedT =0
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)

try:
    while True:
        print("pumping for:", pumpTime)
        GPIO.output(in1, True)
#LED Pattern
        startT= time.time()
        while elapsedT < pumpTime:
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
            endT= time.time()
            elapsedT= endT-startT

        print("Done Pumping")
        GPIO.output(in1, False)

        time.sleep(secondsneeded)

#25 ml per second per pump
#trying to fill 21L

except KeyboardInterrupt:
    GPIO.output(in1, False)
    GPIO.cleanup()
