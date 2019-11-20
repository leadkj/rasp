import Adafruit_PCA9685
import time
 
pwm = Adafruit_PCA9685.PCA9685()
 
 
def set_servo_angle(channel, angle):              
    date=4096*((angle*11)+500)/20000 
    pwm.set_pwm(channel, 0,int(date))
 
pwm.set_pwm_freq(60)
def setup():
    for i in range(4):
        set_servo_angle(i,0)
print('Moving servo on channel x, press Ctrl-C to quit...')
s1=0
s2=0
s3=0
s4=0
sleep=0.01
try:
    while 1:

        if s1==0:
            for i in range(91):
                set_servo_angle(0,i)
                set_servo_angle(1,i)
                time.sleep(sleep)
                s1=i
                s2=i
        else:
            for i in range(91):
                set_servo_angle(0,s1-i)
                set_servo_angle(1,s2-i)
                time.sleep(sleep)
            s1=s1-90
            s2=s2-90
        for i in range(90):
            set_servo_angle(0,s1-i)
            set_servo_angle(1,s2-i)
            time.sleep(sleep)
        s1=s1-90
        s2=s2-90


        if s3==0:
            for i in range(91):
                set_servo_angle(2,i)
                set_servo_angle(3,i)
                time.sleep(sleep)
                s3=i
                s4=i
        else:
            for i in range(91):
                set_servo_angle(2,s1-i)
                set_servo_angle(3,s2-i)
                time.sleep(sleep)
            s3=s3-90
            s4=s4-90
        for i in range(90):
            set_servo_angle(2,s3-i)
            set_servo_angle(3,s4-i)
            time.sleep(sleep)
        s3=s3-90
        s4=s4-90
except KeyboardInterrupt:
    setup()
    print("exit")

