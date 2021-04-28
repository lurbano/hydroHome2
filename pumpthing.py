import RPi.GPIO as GPIO
import time

in1 = 16

pumpRate=25
VolNeeded=21000
pumpTime= VolNeeded/pumpRate
secondsneeded=(60*60*24)-pumpTime

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)

try:
    while True:
        print("PumPiNg nOW")
        print("pumping for:", pumpTime)
        GPIO.output(in1, True)
        time.sleep(pumpTime)
        print("Done Pumping")
        GPIO.output(in1, False)

        time.sleep(secondsneeded)

#25 ml per second per pump
#trying to fill 21L

except KeyboardInterrupt:
    GPIO.output(in1, False)
    GPIO.cleanup()
