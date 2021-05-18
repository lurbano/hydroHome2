import RPi.GPIO as GPIO


in1 = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)

GPIO.output(in1, False)
print("Done Pumping")

GPIO.cleanup()
