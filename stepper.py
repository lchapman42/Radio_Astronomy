from time import sleep
import RPi.GPIO as GPIO

class Stepper():
    def __init__(self, steps_per_rev, initial_ang, pulse_pin, dir_pin):
        self.pulse_pin = pulse_pin
        self.dir_pin = dir_pin
        
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(pulse_pin, GPIO.OUT)
        GPIO.setup(dir_pin, GPIO.OUT)
        
        self.steps_per_rev = steps_per_rev
        self.initial_ang = initial_ang
        print("Steps per revolution =", steps_per_rev)
        print("Initial Angle =", initial_ang)

        self.deg_per_step = 360/steps_per_rev
        self.current_angle = self.initial_ang
        
    def __del__(self):
        GPIO.cleanup()
        print("Destructor called, cleaning up GPIO")

    def pulse(self, fwd):
        sleep(0.001)
        GPIO.output(self.pulse_pin, GPIO.HIGH)
        GPIO.output(self.dir_pin, GPIO.HIGH)

        sleep(0.01)
        GPIO.output(self.pulse_pin, GPIO.LOW)
        
        if (fwd):
            GPIO.output(self.dir_pin, GPIO.LOW)
    
    def pulse_n_times(self, fwd, n):
        print("Pulsed", n, "times")
        for n in range(0, n):
            self.pulse(fwd)

    def go_to_angle(self, new_angle):
        if ((new_angle > 360) or (new_angle < 0)):
            print("Angle given over 360 or negative, using angle mod 360 instead")
            print("New angle:", new_angle % 360)
        new_angle = new_angle % 360

        print("\n---\n")
        print(str(self.current_angle) + u'\N{DEGREE SIGN}', "->", str(new_angle) + u'\N{DEGREE SIGN}')

        if (new_angle - self.current_angle > 0):
            print("Forward")
            steps = int((new_angle - self.current_angle)/self.deg_per_step)

            #print("debug, CAN REMOVE", abs(self.current_angle + (steps+1)*self.deg_per_step - new_angle), ";", abs(self.current_angle + steps*self.deg_per_step - new_angle ))

            if (abs( (steps+1)*self.deg_per_step - new_angle) < abs(self.current_angle + steps*self.deg_per_step - new_angle )):    # checks if error between actual angle and target angle is lower if additional step is added
                steps += 1                                                                                                          # adds addt step if so
            self.current_angle += steps*self.deg_per_step
            self.pulse_n_times(True, steps)

        else:
            print("Reversed")
            steps = int((self.current_angle - new_angle)/self.deg_per_step)
            # print("DEBUG, can remove", abs(self.current_angle - (steps+1)*self.deg_per_step - new_angle), ";", abs(self.current_angle - steps*self.deg_per_step - new_angle ))

            if (abs(self.current_angle - (steps+1)*self.deg_per_step - new_angle) < abs(self.current_angle - steps*self.deg_per_step - new_angle )):     # checks if error between actual angle and target angle is lower if additional step is added
                steps += 1                                                                                                          # adds addt step if so
            self.current_angle -= steps*self.deg_per_step
            self.pulse_n_times(False, steps)

        print("New angle", self.current_angle)
        return self.current_angle

    def change_angle(self, angle_difference):
        if (angle_difference > 360):
            print("Angle given over 360, using angle mod 360 instead")
            print("New angle:", new_angle % 360)
        angle_difference = angle_difference % 360

        print("\n---\n")
        print(str(self.current_angle) + u'\N{DEGREE SIGN}', "->", str(self.current_angle + angle_difference) + u'\N{DEGREE SIGN}')

        if (angle_difference > 0):
            print("Forward")
            steps = int(angle_difference/self.deg_per_step)

            #print("debug, CAN REMOVE", abs(self.current_angle + (steps+1)*self.deg_per_step - new_angle), ";", abs(self.current_angle + steps*self.deg_per_step - new_angle ))

            if (abs( (steps+1)*self.deg_per_step - (self.current_angle + angle_difference)) < abs(self.current_angle + steps*self.deg_per_step - (self.current_angle + angle_difference) )):
                steps += 1
            self.current_angle += steps*self.deg_per_step
            self.pulse_n_times(True, steps)

        else:
            print("Reversed")
            steps = int(angle_difference/self.deg_per_step)
            # print("DEBUG, can remove", abs(self.current_angle - (steps+1)*self.deg_per_step - new_angle), ";", abs(self.current_angle - steps*self.deg_per_step - new_angle ))

            if (abs(self.current_angle - (steps+1)*self.deg_per_step - (self.current_angle + angle_difference)) < abs(self.current_angle - steps*self.deg_per_step - (self.current_angle - angle_difference) )):
                steps += 1
            self.current_angle -= steps*self.deg_per_step
            self.pulse_n_times(False, steps)
