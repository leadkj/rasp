#以下为python源程序
 
#输入通道与角度。即可选通并使该通道的舵机转动到相应的角度
from __future__ import division								#导入 __future__ 文件的 division 功能函数(模块、变量名....)   #新的板库函数  //=
import time
 
# Import the PCA9685 module.
import Adafruit_PCA9685										#导入Adafruit_PCA9685模块
 
 
# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)					#调试打印日志输出
 
import Adafruit_PCA9685
import time
 
pwm = Adafruit_PCA9685.PCA9685()
 
 
def set_servo_angle(tchannel, tangle):              
    date=4096*((tangle*11)+500)/20000 
    pwm.set_pwm(tchannel, 0,int(date))
 
def turn_servo(channel,direction,angle):
	location=0
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
while 1:
    turn_servo(0,1,90)