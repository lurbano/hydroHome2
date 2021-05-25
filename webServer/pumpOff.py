import RPi.GPIO as GPIO
import board
import neopixel
numpix = 20
pixels = neopixel.NeoPixel(board.D18, numpix)
in1 = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)

for i in range(20):
    pixels[i]=(0,0,0)

GPIO.output(in1, False)
print("Done Pumping")

GPIO.cleanup()
