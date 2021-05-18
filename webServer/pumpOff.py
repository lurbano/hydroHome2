

import RPi.GPIO as GPIO
import time
import board
import neopixel
import math
import argparse

in1 = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)



    GPIO.output(in1, False)
    print("Done Pumping")

except KeyboardInterrupt:
    GPIO.output(in1, False)
    GPIO.cleanup()
