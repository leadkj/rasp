# Servo PCA9685.py
# PCA9685 驱动两个舵机的示例

from smbus import SMBus
from PCA9685 import PWM #从PCA9685引入PWM
import time

fPWM = 50
i2c_address = 0x40 # (standard) 根据连接舵机的接口设置I2C地址
channel = 0 # 舵机连接的控制板接口
a = 8.5 # 与舵机相匹配
b = 2  # 与舵机相匹配

def setup():
    global pwm
    bus = SMBus(1) # Raspberry Pi revision 2
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)

def setDirection(direction):
    duty = a / 180 * direction + b
    pwm.setDuty(channel, duty)
    print "direction =", direction, "-> duty =", duty
    time.sleep(1) 
   
print "starting"
setup()
for direction in range(0, 181, 10):
    setDirection(direction)
direction = 0    
setDirection(0)    
print "done"