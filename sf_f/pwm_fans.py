import time
import  RPi.GPIO  as GPIO
import sys
pin =18
fp=50
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
pwm=GPIO.PWM(pin,fp)
pwm.start(0)
try:
  while 1:
    for dc in range(0,101,5):
      pwm.ChangeDutyCycle(dc)
      #time.sleep(3)
except Exception as e:
    print e
    pwm.stop()
    GPIO.cleanup()
