#!/usr/bin/python

# before this worked, had to run the "pigpio daemon" first. 

import pigpio
import time

O = 1175
C = 650
pos = C

servoPin = 18    # this is GPIO18. Pin 12 on the board

pi = pigpio.pi()
pi.set_mode(servoPin, pigpio.OUTPUT)

pi.get_mode(servoPin)


def openBox():
    
    print "opening"
    pos = C
    while pos < O:
        pi.set_servo_pulsewidth(servoPin, pos)
        pos += 2
        time.sleep(.002)
   # pi.stop()

def closeBox():
    print "closing"
    pos = O
    pi = pigpio.pi()
    while pos > C:
        pi.set_servo_pulsewidth(servoPin, pos)
        pos -= 2
        time.sleep(.002)
        
   # pi.stop()

if __name__ == "__main__":
    openBox()
    time.sleep(1)
    closeBox()


#
#print ("mode: ", pi.get_mode(servoPin))
#print("setting to: ",pi.set_servo_pulsewidth(servoPin, 700))
#print("set to: ",pi.get_servo_pulsewidth(servoPin))
#
#time.sleep(1)
#
#print("setting to: ",pi.set_servo_pulsewidth(servoPin, 1225))
#print("set to: ",pi.get_servo_pulsewidth(servoPin))
#
#time.sleep(1)
#
#print("setting to: ",pi.set_servo_pulsewidth(servoPin, 700))
#print("set to: ",pi.get_servo_pulsewidth(servoPin))
#

time.sleep(1)

