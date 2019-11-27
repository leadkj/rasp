'''
四角同步前进,对角同步
'''
import Adafruit_PCA9685
import time
 
pwm = Adafruit_PCA9685.PCA9685()
 
 
def set_servo_angle(channel, angle):              
    date=4096*((angle*11)+500)/20000 
    pwm.set_pwm(channel, 0,int(date))
 
pwm.set_pwm_freq(60)
    
def over():  ##舵机回到初始位置
    print(s0,s1_0,s2_0,s3)
    for i in range(s0):
        set_servo_angle(0,s0-(i+1))
        time.sleep(sleep)
    for i in range(s1):
        set_servo_angle(1,s1-(i+1))
        time.sleep(sleep)
    if s2>90:
        for i in range(s2-90):
            set_servo_angle(2,s2-(i+1))
            time.sleep(sleep)
    elif s2<90:
        for i in range(90-s2):
            set_servo_angle(2,s2+(i+1))
            time.sleep(sleep)
    if s3>90:
        for i in range(s3-90):
            set_servo_angle(3,s3-(i+1))
            time.sleep(sleep)
    elif s3<90:
        for i in range(90-s3):
            set_servo_angle(3,s3+(i+1))
            time.sleep(sleep)
   
print('Moving servo on channel x, press Ctrl-C to quit...')
s1_0=0
s2_0=90
s0=0
s1=0
s2=90
s3=90
sleep=0.01
try:
    while 1:
        print(s0,s1,s2,s3)
        if s0==0:
            for i in range(1,91):
                set_servo_angle(0,i)
                set_servo_angle(3,90-i)
                if s2==0:
                    set_servo_angle(2,i)
                    s2_0=i
                if s1==90:
                    set_servo_angle(1,90-i)
                    s1_0=90-i

                time.sleep(sleep)
                s0=i
                s3=90-i
            s1=0
            s2=90
            print("if1 over s1=0",s1)
             
        else:
            for i in range(1,91):
                set_servo_angle(0,s0-i)
                set_servo_angle(3,90-i)
                time.sleep(sleep)
                s3=90-i
            s0=s0-90

    
        for i in range(1,91):
            set_servo_angle(0,90-i)
            set_servo_angle(3,i)
            set_servo_angle(1,i)
            set_servo_angle(2,90-i)
            time.sleep(sleep)
            s0=90-i  
            s3=i
            s1=i
            s2=90-i
            #s0=0 ,s1=90,s2=0,s3=90
            
        #for i in range(1,91):
        #    set_servo_angle(1,90-i)
        #    set_servo_angle(2,i)
        #    time.sleep(sleep)
        #    s1=s1-1
        #    s2=i
         

        
except KeyboardInterrupt:
    over()
    print("exit")