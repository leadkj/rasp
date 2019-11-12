from __future__ import division								
import time
 

import Adafruit_PCA9685										

 
import Adafruit_PCA9685
import time
 
pwm = Adafruit_PCA9685.PCA9685()
 
 
def set_servo_angle(tchannel, tangle):              
    date=4096*((tangle*11)+500)/20000 
    pwm.set_pwm(tchannel, 0,int(date))
 
def turn_servo(channel,direction,angle,location):
    if direction==1:
        for i in range(angle):
            set_servo_angle(channel, location+i)
            time.sleep(0.01)
        location=angle+location
    elif direction==0:
        if location<angle:
            for i in range(location):
                set_servo_angle(channel,location-i)
                time.sleep(0.01)
            location=0
        else:
            for i in range(angle):
                set_servo_angle(channel,location-i)
                time.sleep(0.01)
            location=location-angle
    else:
        print('please input 1 or 0')


pwm.set_pwm_freq(60)
 
print('Moving servo on channel x, press Ctrl-C to quit...')
location=0

while 1:
    input("aaa")
    turn_servo(0,1,90,location)
    turn_servo(1,1,180,location)