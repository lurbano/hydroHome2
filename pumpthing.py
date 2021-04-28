import RPi.GPIO as GPIO
import time

in1 = 16

pumpRate=25
VolNeeded=21000
pumpTime= VolNeeded/pumpRate
secondsneeded=(60*60*24)-pumpTime

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)

while True:
    GPIO.output(in1, True)
    time.sleep(pumpTime)
    GPIO.output(in1, False)
    print("PumPiNg nOW")
    time.sleep(secondsneeded)

#25 ml per second per pump
#trying to fill 21L


GPIO.cleanup()
