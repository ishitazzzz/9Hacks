import os
import RPi.GPIO as GPIO 
import time 

def buzzer():
    with open('redlist.txt','r') as f:
        x = f.read() 
        if os.path.getsize('./buzzer.py') == 0:
            print("empty")
        else:
            #buzzer code
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(8,GPIO.OUT)
            GPIO.output(8,True)
            #print("buzzer is on")
            time.sleep(1)
            GPIO.OUTPUT(8,False)
            #print(:buzzer is off")
            #time.sleep(1)
            #buzzer code
            #print("intruder detected")
            f.close()
            with open('redlist.txt','w'):
                pass
        f.close()

