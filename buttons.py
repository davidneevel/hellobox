print "buttons"
import RPi.GPIO as GPIO
from time import sleep
import OLEDtext
import responses
import sendEmail

print responses.responses[1]
nResponses = len(responses.responses)
print nResponses

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

rButtPin = 35
lButtPin = 37


GPIO.setup(rButtPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(lButtPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttons():
    prevRBVar = 1
    prevLBVar = 1
    respNum = -1
    resp = 'yes'
    buttonTime = 1
    while buttonTime:
        rBVar = GPIO.input(rButtPin)
        lBVar = GPIO.input(lButtPin)


        
        if(lBVar != prevLBVar):
            if(lBVar == 0):
                print "left button pressed"
                respNum = (respNum + 1) % nResponses
                resp = responses.responses[respNum]
                print resp
                OLEDtext.display(resp)
                sleep(.005)
            if(lBVar == 1):
                print "left button released"
                sleep (.005)
 
        if(rBVar != prevRBVar):
            if(rBVar == 0):
                print "right button pressed"
                buttonTime = 0
                
                sendEmail.sendEmail(resp,"from hellobox")
                sleep(.005)
                
            if(rBVar == 1):
                print "right button released"
                sleep(.005)

        prevRBVar = rBVar
        prevLBVar = lBVar
    print "buttontime is over"
        
   

if __name__ == "__main__":
    buttons()