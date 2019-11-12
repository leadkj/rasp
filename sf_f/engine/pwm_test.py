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
 
 
def set_servo_angle(channel, angle):              
    date=4096*((angle*11)+500)/20000 
    pwm.set_pwm(channel, 0,int(date))
 
pwm.set_pwm_freq(60)
 
angle=0 
print('Moving servo on channel x, press Ctrl-C to quit...')
while 1:
    print(angle)
    f=int(input('forward or back:'))
    if f==1:
        f_angle=int(input('pleas input f_angle:'))
        for i in range(f_angle):
            set_servo_angle(0, angle+i)
            time.sleep(0.01)
        angle=f_angle+angle
    elif f==0:
        b_angle=int(input('pleas input b_angle:'))
        if angle<b_angle:
            for i in range(angle):
                set_servo_angle(0,angle-i)
                time.sleep(0.01)
            angle=0
        else:
            for i in range(b_angle):
                set_servo_angle(0,angle-i)
                time.sleep(0.01)
            angle=angle-b_angle
    else:
        print('please input 1 or 0')