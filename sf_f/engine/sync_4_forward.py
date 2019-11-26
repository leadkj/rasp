'''
四角同步前进
'''
import Adafruit_PCA9685
import time
 
pwm = Adafruit_PCA9685.PCA9685()
 
 
def set_servo_angle(channel, angle):              
    date=4096*((angle*11)+500)/20000 
    pwm.set_pwm(channel, 0,int(date))
 
pwm.set_pwm_freq(60)
    
def over():  ##舵机回到初始位置
    print(s1,s2,s3,s4)
    for i in range(s1):
        set_servo_angle(0,s1-i)
        time.sleep(sleep)
    for i in range(s2):
        set_servo_angle(1,s2-i)
        time.sleep(sleep)
    if s3>90:
        for i in range(s3-90):
            set_servo_angle(2,s3-i)
            time.sleep(sleep)
    elif s3<90:
        print("s3<90")
        for i in range(90-s3):
            set_servo_angle(2,s3+i)
            time.sleep(sleep)
    if s4>90:
        for i in range(s4-90):
            set_servo_angle(3,s4-i)
            time.sleep(sleep)
    elif s4<90:
        print("s4<90")
        for i in range(90-s4):
            set_servo_angle(3,s4+i)
            time.sleep(sleep)
   
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
            print('else1')
            for i in range(91):
                set_servo_angle(0,s1-i)
                set_servo_angle(1,s2-i)
                time.sleep(sleep)
            s1=s1-90
            s2=s2-90
     
        


        if s3==0:
            print('if2')
            for i in range(91):
                set_servo_angle(2,91-i)
                set_servo_angle(3,91-i)
                time.sleep(sleep)
                s3=90-i
                s4=90-i
        else:
            print('else2')
            for i in range(91):
                set_servo_angle(2,91-i)
                set_servo_angle(3,91-i)
                time.sleep(sleep)
                s3=91-i
                s4=91-i
    
        for i in range(90):
            set_servo_angle(0,90-i)
            set_servo_angle(1,90-i)
            time.sleep(sleep)
            s1=s1-1
            s2=s2-1
        for i in range(90):
            print('for2')
            set_servo_angle(2,i)
            set_servo_angle(3,i)
            time.sleep(sleep)
            s3=i
            s4=i
         

        
except KeyboardInterrupt:
    over()
    print("exit")