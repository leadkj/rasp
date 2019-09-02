import picamera
import datetime

def Take_Pic():
    pic_file="pic/Pic%s.jpg"%datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    camera=picamera.PiCamera()
    camera.saturation = 20
    camera.brightness = 40
    camera.iso = 500
    camera.capture(pic_file)
    camera.close()

if __name__=='__main__':
    Take_Pic()
