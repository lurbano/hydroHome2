import RPi.GPIO as GPIO
import time
import board
import neopixel
import math
import argparse



#pump stuff
in1 = 16
pumpRate=25
VolNeeded=21000
pumpTime= VolNeeded/pumpRate
secondsneeded=(60*60*24)-pumpTime
pumptime=10

#LED stuff
timestorun=4
numpix = 20
t=.03
t2=.05
pixels = neopixel.NeoPixel(board.D18, numpix)

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--pump", help = "on or off")
args = parser.parse_args()

#sudo python3 pumpthing.py --pump on

pumpOn=True
if args.pump:
    if args.pump == "off":
        pumpOn = False

elapsedT =0
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)

try:
    while True:
        if pumpOn == False:
            pumpOn=True
        else:
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
                time.sleep(t)
                for i in range(maxLED-1,-1,-1):
                    t2= (5/(i+1))/20
                    bval=i**1.7
                    rval=255-i**1.7
                    pixels[i] = (0,rval,bval)
                    time.sleep(t2)
                    pixels[i] = (0,0,0)
                time.sleep(t)

                endT= time.time()
                elapsedT= endT-startT


            GPIO.output(in1, False)
            print("Done Pumping")

#LED program while idle
        t3=.75
        startT2= time.time()
        elapsedT2=0
        while elapsedT2 < secondsneeded:

            for i in range(20):
                rval=i**1.7
                bval=255-i**1.7
                pixels[i] = (0,rval,bval)
                time.sleep(t3)
                pixels[i] = (0,0,0)
            for i in range(19,-1,-1):
                t4= (5/(i+1))/12
                bval=i**1.7
                rval=255-i**1.7
                pixels[i] = (0,-rval+255,-bval+255)
                time.sleep(t4)
                pixels[i] = (0,0,0)
            endT2= time.time()
            elapsedT2= endT2-startT2

#25 ml per second per pump
#trying to fill 21L

except KeyboardInterrupt:
    GPIO.output(in1, False)
    GPIO.cleanup()
    for i in range(20):
        pixels[i]=(0,0,0)
