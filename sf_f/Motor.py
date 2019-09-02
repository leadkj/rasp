import RPi.GPIO as GPIO 
import time 
import sys 
from array import *
import threading

ports = [12,16,20,21]


def run(clockwise,steps):
    if clockwise==0: 
        arr = [3,2,1,0];
    else:
        arr = [0,1,2,3]
    for i in range(steps):
        for j in arr:
            time.sleep(0.005) 
            for i in range(0,4): 
                if i == j: 
                    GPIO.output(ports[i],True)
                else: 
                    GPIO.output(ports[i],False)
    Stop()
def TRun(c,s):
    
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BCM)

    

    for p in ports: 
        GPIO.setup(p,GPIO.OUT)
    t=threading.Thread(target=run,args=(c,s))
    t.setDaemon(True)
    t.start()
    t.join()
    #Stop()

def Stop():
    try:
        GPIO.setmode(GPIO.BCM)
        for p in ports:
            GPIO.setup(p,0)
        GPIO.cleanup()
    except Exception as e:
        print "e"
    
    
if __name__ == "__main__":
    TRun(0,4000)
    Stop()
