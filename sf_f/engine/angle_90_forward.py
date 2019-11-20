import Adafruit_PCA9685
import time
 
pwm = Adafruit_PCA9685.PCA9685()
 
 
def set_servo_angle(channel, angle):              
    date=4096*((angle*11)+500)/20000 
    pwm.set_pwm(channel, 0,int(date))
 
pwm.set_pwm_freq(60)
print('Moving servo on channel x, press Ctrl-C to quit...')
s1=0
s2=0
sleep=0.01
while 1:

    if s1==0:
        for i in range(91):
            set_servo_angle(0,i)
            time.sleep(sleep)
            s1=i
        print('if1')
    else:
        for i in range(91):
            set_servo_angle(0,s1-i)
            time.sleep(sleep)
        s1=s1-90
    print('for1',s1)
    if s2==0:
        for i in range(91):
            set_servo_angle(1,i)
            time.sleep(sleep)
            s2=i
        print('if2')
    else:
        for i in range(91):
            set_servo_angle(1,s2-i)
            time.sleep(sleep)
        s2=s2-90
    print('for2',s1)
    for i in range(90):
        set_servo_angle(0,s1-i)
        time.sleep(sleep)
    s1=s1-90
    print('for3',s1)
    for i in range(90):
        set_servo_angle(1,s2-i)
        time.sleep(sleep)
    s2=s2-90
    print('for4',s1)

