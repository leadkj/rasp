import Adafruit_PCA9685
import time
 
pwm = Adafruit_PCA9685.PCA9685()
 
 
def set_servo_angle(channel, angle):              
    date=4096*((angle*11)+500)/20000 
    pwm.set_pwm(channel, 0,int(date))
 
pwm.set_pwm_freq(60)
channels=[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
print('Moving servo on channel x, press Ctrl-C to quit...')
while 1:
    print(channels)
    channel=int(input('choice a channel:'))
    angle=channels[channel][-1]
    f=int(input('forward or backward:'))
    if f==1:
        f_angle=int(input('pleas input forward_angle:'))
        for i in range(f_angle):
            set_servo_angle(channel, angle+i)
            time.sleep(0.01)
        angle=f_angle+angle
        channels[channel].append(angle)
    elif f==0:
        b_angle=int(input('pleas input backward_angle:'))
        if angle<b_angle:
            for i in range(angle):
                set_servo_angle(channel,angle-i)
                time.sleep(0.01)
            angle=0
            channels[channel].append(angle)
        else:
            for i in range(b_angle):
                set_servo_angle(channel,angle-i)
                time.sleep(0.01)
            angle=angle-b_angle
            channels[channel].append(angle)
    else:
        print('please input 1 or 0,1 is forward and 0 is backward')
