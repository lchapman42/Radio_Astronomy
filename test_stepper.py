import stepper
from time import sleep

stepper1 = stepper.Stepper(400, 0, 27, 17)
new_angle = 0
stepper1.go_to_angle(45)
sleep(2)
stepper1.go_to_angle(90)
sleep(2)
stepper1.go_to_angle(180)
sleep(2)
stepper1.go_to_angle(270)
sleep(2)
stepper1.go_to_angle(0)
#for i in range(20):
#	angle = stepper1.go_to_angle(new_angle) 
#	new_angle = (angle + 20) % 360
