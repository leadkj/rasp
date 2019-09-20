# -*- coding: utf-8 -*-
import cv2
from ctypes import *
import datetime

user32=windll.LoadLibrary('user32.dll')

def generate():
    stime=datetime.datetime.now()
    face_cascade = cv2.CascadeClassifier(
            r'data\haarcascade_frontalface_alt2.xml')
    videopath='Dangerous.mp4'
    camera = cv2.VideoCapture(0)
    count = 0
    time_c=0

    while (True):
        etime=datetime.datetime.now()
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 检测人脸
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        time_c=time_c+len(faces)
        s=etime-stime
        print s.seconds,time_c
        if s.seconds>20:
            if time_c==0:
                print "window lock"
                user32.LockWorkStation()
            stime = datetime.datetime.now()
            time_c=0
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            f = cv2.resize(gray[y: y+h, x:x+w], (200, 200))
            cv2.imwrite(r'targetPath/%s.jpg' % str(count), frame)
            count += 1
 
        cv2.imshow("camera", frame)

        if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    generate()
