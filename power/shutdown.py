import time
import RPi.GPIO as GPIO
import os,sys

#回调函数，检测GPIO口的电平高低进行相应的操作
def onSwitch(channel):
    if GPIO.input(channel)==GPIO.LOW:
        command='sudo shutdown -h +'+str(timeBeforeShutdown) #使用shutdown指令，表示在timeBeforeShutdown分钟后关机   
        os.system(command) #使用os.system函数执行指令
    else:
        command='sudo shutdown -c' #取消关机的指令
        os.system(command)

timeBeforeShutdown=1 #几分钟后关机

pin_switch=4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin_switch,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#设置为GPIO.BOTH，表示对上升沿和下降沿都进行捕获
GPIO.add_event_detect(pin_switch,GPIO.BOTH,callback=onSwitch)

try:
    while True:
        time.sleep(0.01)    
except:
    print('Close...')
finally:
    GPIO.cleanup()
