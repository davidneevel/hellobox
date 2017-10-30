import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
servoPin = 12
GPIO.setup(servoPin, GPIO.OUT)
servo = GPIO.PWM(servoPin, 100)  # pin 12, 50 Hz


C = 3
O = 5

pos = C


servo.start(C)
sleep(1)

servo.ChangeDutyCycle(O)
sleep(1)
servo.ChangeDutyCycle(C)
   
sleep(1)



GPIO.cleanup()


            
    