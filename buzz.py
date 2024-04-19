import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
while True :
    GPIO.output(8,True)
    #print("buzzer is on")
    time.sleep(1)
    GPIO.OUTPUT(8,False)
    #print(:buzzer is off")
    time.sleep(1)
