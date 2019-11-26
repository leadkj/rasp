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
     
        


        if s8==0:
            for i in range(91):
                set_servo_angle(7,i)
                set_servo_angle(8,i)
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
              
                time.sleep(sleep)
            s8=s8-90
            s9=s9-90
    
        for i in range(90):
            set_servo_angle(0,90-i)
            set_servo_angle(1,90-i)
          
            time.sleep(sleep)
            s1=s1-1
            s2=s2-1
           
        for i in range(90):
            print('for2')
            set_servo_angle(7,90-i)
            set_servo_angle(8,90-i)
          
            time.sleep(sleep)
            s8=s8-1
            s9=s9-1
         

        
except KeyboardInterrupt:
    setup()
    print("exit")