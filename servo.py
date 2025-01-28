import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
p = GPIO.PWM(11,50)
p.start(0)

GPIO.setup(13,GPIO.OUT)
p2 = GPIO.PWM(13,50)
p2.start(0)

angle = 0
duty = angle/18 + 2

p.ChangeDutyCycle(duty)
p2.ChangeDutyCycle(duty)
sleep(1)

p.stop()
p2.stop()
GPIO.cleanup()
quit()

angle = 90
duty = angle/18 + 2

p.ChangeDutyCycle(duty)
p2.ChangeDutyCycle(duty)
sleep(1)

angle = 45
duty = angle/18 + 2

p.ChangeDutyCycle(duty)
p2.ChangeDutyCycle(duty)
sleep(1)

print("Starting cycle")
angle = 0
duty = angle/18 + 2
p.ChangeDutyCycle(duty)
p2.ChangeDutyCycle(duty)
sleep(1)

for i in range(40):
	angle += 15
	angle = (angle % 180)  # cant do more than 180 degrees
	duty = angle/18 + 2
	p.ChangeDutyCycle(duty)
	p2.ChangeDutyCycle(duty)
	sleep(3)
	print("New Angle:", angle, "deg")

p.stop()
p2.stop()
GPIO.cleanup()
