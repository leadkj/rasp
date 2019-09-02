import RPi.GPIO as GPIO
import  sys
args=sys.argv
pin=4
GPIO.setwarnings(False)

def Toff():
    print "off"
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.HIGH)
def Ton():
    print "on" 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
