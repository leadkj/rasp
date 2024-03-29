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
    for i in range(s3):
        set_servo_angle(2,s3-i)
        time.sleep(sleep)
    for i in range(s4):
        set_servo_angle(3,s4-i)
        time.sleep(sleep)
    for i in range(s5):
        set_servo_angle(4,s5-i)
        time.sleep(sleep)
    for i in range(s6):
        set_servo_angle(5,s6-i)
        time.sleep(sleep)
    for i in range(s7):
        set_servo_angle(6,s7-i)
        time.sleep(sleep)
    for i in range(s8):
        set_servo_angle(7,s8-i)
        time.sleep(sleep)
    for i in range(s9):
        set_servo_angle(8,s9-i)
        time.sleep(sleep)
    for i in range(s10):
        set_servo_angle(9,s10-i)
        time.sleep(sleep)
    for i in range(s11):
        set_servo_angle(10,s11-i)
        time.sleep(sleep)
    for i in range(s12):
        set_servo_angle(11,s12-i)
        time.sleep(sleep)
    for i in range(s13):
        set_servo_angle(12,s13-i)
        time.sleep(sleep)
    for i in range(s14):
        set_servo_angle(13,s14-i)
        time.sleep(sleep)
print('Moving servo on channel x, press Ctrl-C to quit...')
s1=0
s2=0
s3=0
s4=0
s5=0
s6=0
s7=0
s8=0
s9=0
s10=0
s11=0
s12=0
s13=0
s14=0
sleep=0.01
try:
    while 1:

        if s1==0:
            for i in range(91):
                set_servo_angle(0,i)
                set_servo_angle(1,i)
                set_servo_angle(2,i)
                set_servo_angle(3,i)
                set_servo_angle(4,i)
                set_servo_angle(5,i)
                set_servo_angle(6,i)
                time.sleep(sleep)
                s1=i
                s2=i
                s3=i
                s4=i
                s5=i
                s6=i
                s7=i
        else:
            print('else1')
            for i in range(91):
                set_servo_angle(0,s1-i)
                set_servo_angle(1,s2-i)
                set_servo_angle(2,s3-i)
                set_servo_angle(3,s4-i)
                set_servo_angle(4,s5-i)
                set_servo_angle(5,s6-i)
                set_servo_angle(6,s7-i)
                time.sleep(sleep)
            s1=s1-90
            s2=s2-90
            s3=s3-90
            s4=s4-90
            s5=s5-90
            s6=s6-90
            s7=s7-90
        


        if s8==0:
            for i in range(91):
                set_servo_angle(7,i)
                set_servo_angle(8,i)
                set_servo_angle(9,i)
                set_servo_angle(10,i)
                set_servo_angle(11,i)
                set_servo_angle(12,i)
                set_servo_angle(13,i)
                time.sleep(sleep)
                s8=i
                s9=i
                s10=i
                s11=i
                s12=i
                s13=i
                s14=i
        else:
            print('else1')
            for i in range(91):
                set_servo_angle(7,s1-i)
                set_servo_angle(8,s2-i)
                set_servo_angle(9,s3-i)
                set_servo_angle(10,s4-i)
                set_servo_angle(11,s5-i)
                set_servo_angle(12,s6-i)
                set_servo_angle(13,s7-i)
                time.sleep(sleep)
            s8=s8-90
            s9=s9-90
            s10=s10-90
            s11=s11-90
            s12=s12-90
            s13=s13-90
            s14=s14-90
        for i in range(90):
            set_servo_angle(0,90-i)
            set_servo_angle(1,90-i)
            set_servo_angle(2,90-i)
            set_servo_angle(3,90-i)
            set_servo_angle(4,90-i)
            set_servo_angle(5,90-i)
            set_servo_angle(6,90-i)
            time.sleep(sleep)
            s1=s1-1
            s2=s2-1
            s3=s3-1
            s4=s4-1
            s5=s5-1
            s6=s6-1
            s7=s7-1
        for i in range(90):
            print('for2')
            set_servo_angle(7,90-i)
            set_servo_angle(8,90-i)
            set_servo_angle(9,90-i)
            set_servo_angle(10,90-i)
            set_servo_angle(11,90-i)
            set_servo_angle(12,90-i)
            set_servo_angle(13,90-i)
            time.sleep(sleep)
            s8=s8-1
            s9=s9-1
            s10=s10-1
            s11=s11-1
            s12=s12-1
            s13=s13-1
            s14=s14-1

        
except KeyboardInterrupt:
    setup()
    print("exit")