import RPi.GPIO as GPIO
from time import sleep
import sys

angle1 = float(sys.argv[1])
angle2 = float(sys.argv[2])

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
p = GPIO.PWM(11,50)
p.start(0)

GPIO.setup(13,GPIO.OUT)
p2 = GPIO.PWM(13,50)
p2.start(0)

duty1 = angle1/18 + 2
duty2 = angle2/18 + 2

p.ChangeDutyCycle(duty1)
p2.ChangeDutyCycle(duty2)
sleep(1)

p.stop()
p2.stop()
GPIO.cleanup()

