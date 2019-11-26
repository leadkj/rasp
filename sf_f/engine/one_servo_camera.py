import Adafruit_PCA9685
import time
 
pwm = Adafruit_PCA9685.PCA9685()
 
 
def set_servo_angle(channel, angle):              
    date=4096*((angle*11)+500)/20000 
    pwm.set_pwm(channel, 0,int(date))
 
pwm.set_pwm_freq(60)
def setup():  ##舵机回到初始位置
    for i in range(s1):
        set_servo_angle(0,s1-i)
        time.sleep(sleep)
print('Moving servo on channel x, press Ctrl-C to quit...')
s1=0

sleep=0.01
try:
    while 1:

        if s1==0:
            for i in range(91):
                set_servo_angle(4,i)
                time.sleep(sleep)
                s1=i
        
        else:
            print('else1')
            for i in range(91):
                set_servo_angle(4,s1-i)
                time.sleep(sleep)
            s1=s1-90

        


   
        for i in range(90):
            set_servo_angle(4,90-i)

            s1=s1-1
  
except KeyboardInterrupt:
    setup()
    print("exit")