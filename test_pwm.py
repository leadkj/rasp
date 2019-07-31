# -*- coding: utf-8 -*-
 
import RPi.GPIO as GPIO
import time,sys
 
# 控制风扇的GPIO
FAN_GPIO = 11
# 低温阈值，低于它则关闭风扇
MIN_TEMP = 35
# 高温阈值，高于它则全速运转
MAX_TEMP = 55
# 多长时间读取一次CPU温度，单位秒
SAMPLING = 30

cycle=sys.argv[1]
 
def main(cycle):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(FAN_GPIO, GPIO.OUT)
 
    # 初始化PWM的频率，frequency=50Hz
    pwm = GPIO.PWM(FAN_GPIO, 50)
    # 为防止风扇卡死，开机全速运行n秒
    pwm.start(100)
    time.sleep(5)
    pwm.stop()
    
    pwm.start(cycle)

if __name__ == "__main__":
  main(cycle)
