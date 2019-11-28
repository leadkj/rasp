'''
8舵机同步模拟四脚前进，对角同步，腿关节抬，膝关节落
'''
import Adafruit_PCA9685
import time
 
pwm = Adafruit_PCA9685.PCA9685()
 
 
def set_servo_angle(channel, angle):              
    date=4096*((angle*11)+500)/20000 
    pwm.set_pwm(channel, 0,int(date))
 
pwm.set_pwm_freq(60)
    
def over():  ##舵机回到初始位置
    ##0号舵机恢复到初始位置
    for i in range(s0):
        set_servo_angle(0,s0-(i+1))
        time.sleep(sleep)
    
    ##1号舵机恢复到初始位置
    _s1=(s1 if s1>s1_0 and s1!=90 else s1_0) if s1_0!=90 else s1 ####s1,s1_0在不能与0或者90的情况下，以数值大的一个为恢复到原始位置的角度
    for i in range(_s1):
        set_servo_angle(1,_s1-(i+1))
        time.sleep(sleep)
    
    #2号舵机恢复到初始位置
    if s2>90:
        _s2=(s2 if s2>s2_0 and s2!=90 else s2_0) if s2_0!=90 else s2
        for i in range(_s2-90):
            set_servo_angle(2,_s2-(i+1))
            time.sleep(sleep)
    elif s2<90:
        _s2=(s2 if s2>s2_0 and s2!=90 else s2_0) if s2_0!=90 else s2
        for i in range(90-_s2):
            set_servo_angle(2,_s2+(i+1))
            time.sleep(sleep)
    #3号舵机恢复到初始位置
    if s3>90:
        for i in range(s3-90):
            set_servo_angle(3,s3-(i+1))
            time.sleep(sleep)
    elif s3<90:
        for i in range(90-s3):
            set_servo_angle(3,s3+(i+1))
            time.sleep(sleep)
    
    ###4号膝关节舵机恢复到初始位置
    for i in range(s4):
        set_servo_angle(4,s4-(i+1))
        time.sleep(sleep)
    ###5号膝关节舵机恢复到初始位置
    for i in range(s5_0):
        set_servo_angle(5,s5_0-(i+1))
        time.sleep(sleep)
    ###6号膝关节舵机恢复到初始位置
    if s6_0>60:
        for i in range(s6_0-60):
            set_servo_angle(6,s6_0-(i+1))
            time.sleep(sleep)
    elif s6_0<60:
        for i in range(60-s6_0):
            set_servo_angle(6,s6_0+(i+1))
            time.sleep(sleep)
    ###7号膝关节舵机恢复到初始位置
    if s7>60:
        for i in range(s7-60):
            set_servo_angle(7,s7-(i+1))
            time.sleep(sleep)
    elif s7<60:
        for i in range(60-s7):
            set_servo_angle(7,s7+(i+1))
            time.sleep(sleep)
   
print('Moving servo on channel x, press Ctrl-C to quit...')


b_leg=90  ######大腿轴旋转度数


s_leg=60  ########膝关节度数

##每个舵机初始位置
s1_0=0  ##记录1号过程中的角度
s2_0=90 ##记录2号过程中的角度
s0=0
s1=0
s2=90
s3=90
##########膝关节
s4=0
s5=0
s5_0=0  #记录5号过程中的角度
s6=0
s6_0=90  #记录6号过程中的角度
s7=0




sleep=0.01
try:
    while 1:
        print(s0,s1,s2,s3)
        ####舵机往复运动之前进
        if s0==0:
            for i in range(1,b_leg+1):

                ###########右前腿舵机##############
                set_servo_angle(0,i)
                s0=i
                ###膝关节##
                if i<=60:
                    set_servo_angle(4,i)
                    s4=i

                ###################################

                ###########左后腿舵机##############
                set_servo_angle(3,b_leg-i)
                s3=90-i
                ###膝关节##
                if i<=60:
                    set_servo_angle(7,60-i)
                    s7=60-i
                ###################################

                ###########左前腿舵机##############
                if s2==0:
                    set_servo_angle(2,i)
                    s2_0=i
                ###膝关节##
                    if i<=60:
                        set_servo_angle(6,i)
                        s6_0=i
                ###################################

                ###########右后腿舵机##############
                if s1==90:
                    set_servo_angle(1,b_leg-i)
                    s1_0=90-i
                ###膝关节##
                    if i<=60:
                        set_servo_angle(5,s5-i)
                        s5_0=60-i
                ###################################
                time.sleep(sleep)
            s1=0
            s2=90
            s5=0
            s6=60
        else:
            for i in range(1,91):
                set_servo_angle(0,s0-i)
                set_servo_angle(3,90-i)
                time.sleep(sleep)
                s3=90-i
            s0=s0-90

        ####舵机往复运动之回位
        for i in range(1,91):
            ###########右前腿舵机##########
            set_servo_angle(0,90-i)
            s0=90-i
            ###膝关节###
            if i<=60:
                set_servo_angle(4,s4-i)
                s4=60-i
            ###############################

            ###########左后腿舵机##########
            set_servo_angle(3,i)
            s3=i
            ###膝关节###
            if i<=60:
                set_servo_angle(7,i)
                s7=i

            ###############################

            ###########右后腿舵机##########
            set_servo_angle(1,i)
            s1=i
            ###膝关节###
            if i<=60:
                set_servo_angle(5,i)
                s5_0=i
                s5=i
            ###############################

            ###########左前腿舵机##########
            set_servo_angle(2,90-i)
            s2=90-i
            ###膝关节###
            if i<=60:
                set_servo_angle(6,60-i)
                s6=60-i
            ###############################
            time.sleep(sleep)
              
except KeyboardInterrupt:
    over()
    print("exit")