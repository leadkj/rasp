#coding:utf-8
import Adafruit_DHT


def Get_T_H():
    sensor=Adafruit_DHT.DHT22
    pin=4
    humidity,temperature=Adafruit_DHT.read_retry(sensor,pin)
    return humidity,temperature



if __name__=='__mian__':
   h,t= Get_T_H()
   print h,t
    
