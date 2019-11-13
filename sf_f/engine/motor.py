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