import Adafruit_PCA9685
import time
 
pwm = Adafruit_PCA9685.PCA9685()
 
 
def set_servo_angle(channel, angle):              
    date=4096*((angle*11)+500)/20000 
    pwm.set_pwm(channel, 0,int(date))
 
pwm.set_pwm_freq(60)
def setup():  ##舵机回到初始位置
    print(s1,s2,s3,s4)
    for i in range(s1):
        set_servo_angle(0,s1-i)
        time.sleep(sleep)
    for i in range(s2):
        set_servo_angle(1,s2-i)
        time.sleep(sleep)
print('Moving servo on channel x, press Ctrl-C to quit...')
s1=0
s2=0
s3=0
s4=0
sleep=0
try:
    while 1:

        if s1==0:
            print('if')
            for i in range(91):
                set_servo_angle(0,i)
                s1=i
                if i <=45:
                    set_servo_angle(1,i)
                    s2=i
                time.sleep(sleep)
        else:
            print('else')
            for i in range(91):
                set_servo_angle(0,s1-i)
                if i<=45:
                    print(s2)
                    set_servo_angle(1,s2-i)
                time.sleep(sleep)
            s1=s1-90
            s2=s2-45
        
        print(s2)

        for i in range(90):
            set_servo_angle(0,90-i)
            s1=s1-1
            if i<=44:
                set_servo_angle(1,45-i)
                s2=s2-1
            time.sleep(sleep)
except KeyboardInterrupt:
    setup()
    print("exit")