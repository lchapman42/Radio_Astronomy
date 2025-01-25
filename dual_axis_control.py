import stepper

elevation_stp   = stepper.Stepper(steps_per_rev=400, initial_ang=0, pulse_pin=17, dir_pin=27) # use GPIO pin numbers
azimuth_stp     = stepper.Stepper(steps_per_rev=400, initial_ang=0, pulse_pin=23, dir_pin=24)

print("Updating Elevation Stepper to 15 deg")
elevation_stp.go_to_angle(15)
print("Updating Azimuth Stepper to 30 deg")
azimuth_stp.go_to_angle(30)

print("Changing Elevation Stepper by 5 deg")
elevation_stp.change_angle(5)
print("Changing Azimuth Stepper by 10 deg")
azimuth_stp.change_angle(10)

print("Changing Elevation Stepper by -10 deg")
elevation_stp.change_angle(-10)
print("Changing Azimuth Stepper by -5 deg")
azimuth_stp.change_angle(-5)

print("Updating Elevation Stepper to 5 deg")
elevation_stp.go_to_angle(5)
print("Updating Azimuth Stepper to 20 deg")
azimuth_stp.go_to_angle(20)

print("Test complete")
