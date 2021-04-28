import RPi.GPIO as GPIO
import time

in1 = 16


GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)


GPIO.output(in1, False)


GPIO.output(in1, True)
time.sleep(5)
GPIO.output(in1, False)





GPIO.cleanup()
