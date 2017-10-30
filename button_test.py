print "button test"
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

rButtPin = 35
lButtPin = 37
prevRBVar = 1
prevLBVar = 1

GPIO.setup(rButtPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(lButtPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    rBVar = GPIO.input(rButtPin)
    lBVar = GPIO.input(lButtPin)
  
    
    if(rBVar != prevRBVar):
        if(rBVar == 0):
            print "right button pressed"
            sleep(.005)
        if(rBVar == 1):
            print "right button released"
            sleep(.005)
            
    if(lBVar != prevLBVar):
        if(lBVar == 0):
            print "left button pressed"
            sleep(.005)
        if(lBVar == 1):
            print "left button released"
            sleep (.005)
    prevRBVar = rBVar
    prevLBVar = lBVar
   